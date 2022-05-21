from src.constants import (
    COIN_TOSS_TO_FUTURE_INDEX,
    COIN_TOSS_TO_FUTURE_SCHEMA,
    COIN_TOSS_TO_PRESENT_INDEX,
    COIN_TOSS_TO_PRESENT_SCHEMA,
    LINE_INDICES_TO_TRIGRAM_INDEX,
)
from src.errors import SchemaError
from validators.coin_tosses import CoinTossesValidator
from validators.trigram_schema import TrigramSchemaValidator

class TrigramSchema:
    def __init__(
        self,
        coin_tosses: list,
        schema_type: str,
        validate_coin_tosses: bool
    ):
        if validate_coin_tosses:
            CoinTossesValidator(coin_tosses)

        if schema_type in ['present', 'future']:
            self.schema_type = schema_type
        else:
            raise SchemaError(f'Invalid schema type {schema_type} provided.')
        
        self.schema = None
        self.index = None
        self.__prepare(coin_tosses)

        TrigramSchemaValidator(self.schema, self.index, self.schema_type)
    
    def __prepare(self, coin_tosses: list) -> None:
        if self.schema_type == 'present':
            line_map = COIN_TOSS_TO_PRESENT_SCHEMA
            index_map = COIN_TOSS_TO_PRESENT_INDEX
        else:
            line_map = COIN_TOSS_TO_FUTURE_SCHEMA
            index_map = COIN_TOSS_TO_FUTURE_INDEX
        
        self.schema = '\n'.join((line_map[toss] for toss in coin_tosses))
        line_index = tuple((index_map[toss] for toss in coin_tosses))
        self.index = LINE_INDICES_TO_TRIGRAM_INDEX[line_index]


        
