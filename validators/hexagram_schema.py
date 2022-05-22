from src.errors import SchemaError
from src.constants import HEXAGRAM_LENGTH, NUMBER_OF_HEXAGRAMS


class HexagramSchemaValidator:
    """
    Validator for Hexagram Schemas.
    """
    def __init__(self, schema: str, index: int, schema_type: str):
        self.__validate_schema(schema, index, schema_type)

    def __validate_schema(self, schema: str, index: int, schema_type: str) -> None:
        if schema_type not in ['present', 'future']:
            raise SchemaError(f'Hexagram Schema has invalid Schema type: {schema_type}.')
        if not isinstance(schema, str):
            raise SchemaError(f'The {schema_type} Hexagram schema is not a string.')
        if schema.count('\n') != HEXAGRAM_LENGTH - 1:
            raise SchemaError(f'The {schema_type} Hexagram schema is incorrect. Try building the Schema again.')

        if not isinstance(index, int):
            raise SchemaError('The Schema index is not an integer.')
        if not 1 <= index <= NUMBER_OF_HEXAGRAMS:
            raise SchemaError(f'The {schema_type} Hexagram has incorrect index {index}.')
