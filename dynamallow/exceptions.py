import logging

log = logging.getLogger(__name__)


# --- Schema exceptions ---
class MarshModelException(Exception):
    """Base exception for MarshModel problems"""


class ValidationError(MarshModelException):
    """Schema validation failed"""
    def __init__(self, raw, schema_name, errors, *args, **kwargs):
        super(ValidationError, self).__init__(*args, **kwargs)
        self.errors = errors
        self.raw = raw
        self.schema_name = schema_name

    def __unicode__(self):
        log.debug('Validation failure for data: {0}'.format(self.raw))
        return 'Validation failed for schema {0}. Errors: {1}'.format(
            self.schema_name, self.errors
        )

    def __str__(self):
        log.debug('Validation failure for data: {0}'.format(self.raw))
        return 'Validation failed for schema {0}. Errors: {1}'.format(
            self.schema_name, self.errors
        )


# --- Table exceptions ---
class DynamoTableException(Exception):
    """Base exception class for all DynamoTable errors"""


class MissingTableAttribute(DynamoTableException):
    """A required attribute is missing"""


class InvalidSchemaField(DynamoTableException):
    """A field provided does not exist in the schema"""


class InvalidKey(DynamoTableException):
    """A parameter is not a valid key"""


class HashKeyExists(DynamoTableException):
    """A operating requesting a unique hash key failed"""
