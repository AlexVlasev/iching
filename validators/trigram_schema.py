from src.errors import SchemaError
from src.constants import TRIGRAM_LENGTH, NUMBER_OF_TRIGRAMS


class TrigramSchemaValidator:
    """
    Validator for Trigram Schemas.
    """
    def __init__(self, schema: str, index: int, schema_type: str):
        self.__validate_schema(schema, index, schema_type)

    def __validate_schema(self, schema: str, index: int, schema_type: str) -> None:
        if schema_type not in ['present', 'future']:
            raise SchemaError(f'Trigram Schema has invalid Schema type: {schema_type}.')

        if not isinstance(schema, str):
            raise SchemaError(f'The {schema_type} Trigram schema is not a string.')
        if schema.count('\n') != TRIGRAM_LENGTH - 1:
            raise SchemaError(f'The {schema_type} Trigram schema is incorrect. Try building the Schema again.')

        if not isinstance(index, int):
            raise SchemaError('The Trigram Schema index is not an integer.')
        if not 1 <= index <= NUMBER_OF_TRIGRAMS:
            raise SchemaError(f'The {schema_type} Trigram has incorrect index {index}.')
