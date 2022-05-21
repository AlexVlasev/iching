from src.errors import SchemaError
from src.constants import HEXAGRAM_LENGTH, NUMBER_OF_HEXAGRAMS


class HexagramSchemaValidator:
    def __init__(self, schema: str, index: int, schema_type: str):
        self.__validateSchema(schema, index, schema_type)

    def __validateSchema(self, schema: str, index: int, schema_type: str) -> None:
        if schema_type not in ['present', 'future']:
            raise SchemaError(f'Hexagram Schema has invalid Schema type: {schema_type}')

        if type(schema) is not str:
            raise SchemaError(f'The {schema_type} Hexagram schema is not a string.')
        if schema.count('\n') != HEXAGRAM_LENGTH - 1:
            raise SchemaError(f'The {schema_type} Hexagram schema is incorrect. Try building the Schema again.')
        
        if type(index) is not int:
            raise SchemaError(f'The ')
        if not 1 <= index <= NUMBER_OF_HEXAGRAMS:
            raise SchemaError(f'The {schema_type} Hexagram has incorrect index {index}.')
