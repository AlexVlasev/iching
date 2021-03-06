from schemas.hexagram_schema import HexagramSchema
from validators.coin_tosses import CoinTossesValidator
from validators.hexagram_schema import HexagramSchemaValidator
from validators.trigram_schema import TrigramSchemaValidator

from .errors import HexagramError, TrigramError
from .trigram import Trigram


class Hexagram:
    """
    The Hexagram class provides a simple API to convert two Trigrams
    into a Hexagram. There are a number of checks and validations along the way.

    Once the Trigrams are validated, a Hexagram is constructed. Then a user
    can obtain its schema and/or index directly.

    TODO: create getters for the schema and for the index.
    """
    def __init__(self, lower_trigram: Trigram, upper_trigram: Trigram):
        self.lower_trigram = None
        self.upper_trigram = None

        self.schemas = dict()

        self.__validate_trigram(lower_trigram)
        self.__validate_trigram(upper_trigram)

        self.__prepare(lower_trigram, upper_trigram)
        self.__validate()

    def __validate_trigram(self, trigram: Trigram) -> None:
        if not isinstance(trigram, Trigram):
            raise TrigramError('Invalid Trigram object provided to Hexagram.')

        CoinTossesValidator(trigram.coin_tosses)
        for schema in trigram.schemas.values():
            TrigramSchemaValidator(schema.schema, schema.index, schema.schema_type)

    def __prepare(self, lower_trigram: Trigram, upper_trigram: Trigram) -> None:
        self.schemas['present'] = HexagramSchema(lower_trigram, upper_trigram, 'present', False)
        self.schemas['future'] = HexagramSchema(lower_trigram, upper_trigram, 'future', False)

    def validate(self) -> None:
        """
        Use the validation logic yourself.
        """
        self.__validate()

    def __validate(self) -> None:
        if len(self.schemas) != 2:
            raise HexagramError('The number of schemas is incorrect')
        for schema in self.schemas.values():
            HexagramSchemaValidator(schema.schema, schema.index, schema.schema_type)
