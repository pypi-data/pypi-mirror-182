"""Module to manage EDS schema configurations.

Configurations are drawn from a local schema configuration file.
The file must be named 'schema.yaml', and be accessible at the root of the project.
the file must be formatted using YAML.

To examine the current configuration from a Python shell:

    >>> from rbx.eds.config import schemas
    >>> schema.DIMENSIONS

"""
from collections.abc import Mapping
from importlib import resources
import logging
import os

from google.cloud.bigquery import SchemaField
from sqlalchemy import (BINARY, DECIMAL, Boolean, Column, Float, Index, Integer, MetaData, String,
                        Table, Text)
from sqlalchemy.dialects.mysql import DATETIME

import yaml

from . import Aggregate, Dimension, Fact

logger = logging.getLogger(__name__)

types = {
    'BINARY': BINARY(20),
    'BOOLEAN': Boolean,
    'DECIMAL': DECIMAL(12, 6),
    'INTEGER': Integer,
    'FLOAT': Float,
    'STRING': String,
    'TEXT': Text,
    'TIMESTAMP': DATETIME(fsp=6),
}


def _parse_field_type(field):
    field_type = types[field['type']]

    if field['type'] == 'STRING':
        field_length = field.get('length', 255)
        if field_length == 'TEXT':
            field_type = Text
        else:
            field_type = types[field['type']](field_length)

    return field_type


def _table_for_aggregate(aggregate, metadata):
    """The database metadata using the SQLAlchemy representation.

    An aggregate table may have multiple Primary Keys.
    """
    fields = [
        Column(
            field['name'],
            _parse_field_type(field),
            autoincrement=field.get('autoincrement', False),
            default=field.get('default', None),
            index=field.get('index', False),
            nullable=field.get('nullable', False),
            primary_key=field.get('primary_key', False),
            server_default=str(field['default']) if 'default' in field else None,
            unique=field.get('unique', False),
        )
        for field in aggregate['schema']
    ]

    return Table(aggregate['name'], metadata, *fields, mysql_charset='utf8mb4')


def _tables_for_dimension(dimension, metadata):
    """The database metadata using the SQLAlchemy representation.

    The first field in the ordered list of fields is always assumed to be the Primary Key, unless
    it is specified.

    The meta will always include 2 tables, one for the table, and one for its staging table.
    """
    name = dimension['key']
    schema = dimension['schema']

    primary_key = next(
        (field for field in schema if field.get('primary_key', False) is True),
        None
    )
    if not primary_key:
        primary_key = schema[0]

    fields = [Column(primary_key['name'], Integer, primary_key=True, autoincrement=False)]
    fields_staging = [Column(primary_key['name'], Integer, primary_key=True, autoincrement=False)]

    secondary_fields = [field for field in schema if field['name'] != primary_key['name']]
    for field in secondary_fields:
        index = False
        composite_index = False
        if field['name'] in dimension.get('index_fields', []):
            if field.get('length') == 'TEXT':
                composite_index = True
            else:
                index = True

        fields.append(Column(
            field['name'],
            _parse_field_type(field),
            index=index
        ))
        fields_staging.append(Column(
            field['name'],
            _parse_field_type(field),
            index=index
        ))

        if composite_index:
            fields.append(Index(
                f"ix_{name}_{field['name']}",
                f"{field['name']}",
                mysql_length=255
            ))
            fields_staging.append(Index(
                f"ix_{name}_staging_{field['name']}",
                f"{field['name']}",
                mysql_length=255
            ))

    return {
        name: Table(name, metadata, *fields, mysql_charset='utf8mb4'),
        name + '_staging': Table(name + '_staging', metadata, *fields_staging,
                                 mysql_charset='utf8mb4'),
    }


def _parse_yaml_config(data, metadata):
    """Parse the YAML configuration data into a dictionary.

    For example:

        dimensions:
          -
            name: string
            key: string

        facts:
          -
            name: string

    Becomes:

        {
            'DIMENSIONS': {
                'key': Dimension(name='string')
            },
            'FACTS': {
                'name': Fact(name='string')
            },
            'PURE_DIMENSIONS': {}
        }

    Dimensions are pure when they have a schema and are model-based.
    """
    values = {}
    if not data:
        return values
    try:
        content = yaml.load(data, Loader=yaml.FullLoader)
    except yaml.parser.ParserError:
        return values

    if 'aggregates' in content:
        values['AGGREGATES'] = {}
        for aggregate in content['aggregates']:
            aggregate['table'] = _table_for_aggregate(aggregate, metadata)
            aggregate['schema'][:] = [
                SchemaField(field['name'], field['type'],
                            'NULLABLE' if field.get('nullable', False) else 'REQUIRED')
                for field in aggregate['schema']
            ]
            values['AGGREGATES'][aggregate['name']] = Aggregate(**aggregate)

    if 'dimensions' in content:
        values['DIMENSIONS'] = {}
        for dimension in content['dimensions']:
            if 'key' in dimension:
                if 'schema' in dimension:
                    dimension['tables'] = _tables_for_dimension(dimension, metadata)
                    dimension['schema'][:] = [
                        SchemaField(field['name'], field['type'], field.get('mode', 'NULLABLE'))
                        for field in dimension['schema']
                    ]
                values['DIMENSIONS'][dimension['key']] = Dimension(**dimension)

        values['PURE_DIMENSIONS'] = {}
        for key, value in values['DIMENSIONS'].items():
            if value.model_based and value.schema:
                values['PURE_DIMENSIONS'][key] = value

    if 'facts' in content:
        values['FACTS'] = {}
        for fact in content['facts']:
            try:
                fact['schema'][:] = [
                    SchemaField(field['name'], field['type'],
                                'REQUIRED' if field['required'] else 'NULLABLE')
                    for field in fact['schema']
                ]
                values['FACTS'][fact['name']] = Fact(**fact)
            except KeyError:
                pass

    # All other sections are returned without further processing
    values.update({
        key.upper(): value
        for key, value in content.items()
        if key not in ('aggregates', 'dimensions', 'facts')
    })

    return values


def _configure(metadata):
    """This function loads the schema configuration from the YAML file.

    The sript will first attempt to locate the file at the root of the project. Or at the custom
    location given via the 'SCHEMA_YAML_PATH' environment variable.

    If the file does not exist, the script will cycle through all elligible packages and use the
    first one it finds. Elligible packages are defined via the 'SCHEMA_PACKAGES' environment
    variable.
    """
    defaultpath = os.path.join(os.path.dirname('__FILE__'), 'schema.yaml')
    filepath = os.getenv('SCHEMA_YAML_PATH', defaultpath)
    logger.debug(f'Loading config from "{filepath}"')
    try:
        with open(filepath, 'rb') as fd:
            content = fd.read()

        return _parse_yaml_config(content, metadata)

    except FileNotFoundError as e:
        logger.debug(e)

        packages = os.getenv('SCHEMA_PACKAGES')
        if packages:
            for package in packages.split(','):
                logger.debug(f'Loading config from "{package}" package')
                try:
                    data = resources.read_binary(package, 'schema.yaml')
                except FileNotFoundError as e:
                    logger.debug(e)
                    continue
                else:
                    return _parse_yaml_config(data, metadata)

    raise NotImplementedError('A valid schema file could not be located.')


class Schema(Mapping):
    """Lazy loader of schema data."""
    def __init__(self, metadata):
        self._data = None
        self.metadata = metadata

    @property
    def data(self):
        if self._data is None:
            self._data = _configure(metadata=self.metadata)
        return self._data

    def __getitem__(self, key):
        return self.data.get(key)

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __getattr__(self, name):
        return self[name]


schema = Schema(metadata=MetaData())

__all__ = ['schema']
