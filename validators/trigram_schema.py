from src.errors import SchemaError
from src.constants import TRIGRAM_LENGTH, NUMBER_OF_TRIGRAMS


class TrigramSchemaValidator:
    def __init__(self, schema: str, index: int, schema_type: str):
        self.__validateSchema(schema, index, schema_type)

    def __validateSchema(self, schema: str, index: int, schema_type: str) -> None:
        if schema_type not in ['present', 'future']:
            raise SchemaError(f'Trigram Schema has invalid Schema type: {schema_type}')

        if type(schema) is not str:
            raise SchemaError(f'The {schema_type} Trigram schema is not a string.')
        if schema.count('\n') != TRIGRAM_LENGTH - 1:
            raise SchemaError(f'The {schema_type} Trigram schema is incorrect. Try building the Schema again.')
        
        if type(index) is not int:
            raise SchemaError(f'The ')
        if not 1 <= index <= NUMBER_OF_TRIGRAMS:
            raise SchemaError(f'The {schema_type} Trigram has incorrect index {index}.')
