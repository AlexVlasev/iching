from schemas.trigram_schema import TrigramSchema
from validators.coin_tosses import CoinTossesValidator
from validators.trigram_schema import TrigramSchemaValidator

from .errors import TrigramError


class Trigram:
    """
    The Trigram class provides a simple API to convert coin tosses into a Trigram
    that is then used for constructing a Hexagram. There are a number of
    checks and validations along the way.

    Once the coin tosses are validated, the Trigram is constructed. Then a user
    can obtain its schema and/or index directly.

    TODO: create getters for the schema and for the index.
    """
    def __init__(self, coin_tosses: list):
        self.coin_tosses = None
        self.schemas = dict()

        CoinTossesValidator(coin_tosses)
        self.__prepare(coin_tosses)
        self.__validate()

    def __prepare(self, coin_tosses: list) -> None:
        self.coin_tosses = coin_tosses
        self.schemas['present'] = TrigramSchema(coin_tosses, 'present', False)
        self.schemas['future'] = TrigramSchema(coin_tosses, 'future', False)

    def validate(self) -> None:
        """
        You can use the internal validation logic yourself.
        """
        self.__validate()

    def __validate(self) -> None:
        if len(self.schemas) != 2:
            raise TrigramError('The number of schemas is incorrect')
        for schema in self.schemas.values():
            TrigramSchemaValidator(schema.schema, schema.index, schema.schema_type)
