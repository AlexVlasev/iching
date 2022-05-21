from .constants import (
    COIN_TOSS_TO_FUTURE_INDEX,
    COIN_TOSS_TO_FUTURE_SCHEMA,
    COIN_TOSS_TO_PRESENT_INDEX,
    COIN_TOSS_TO_PRESENT_SCHEMA,
    LINE_INDICES_TO_TRIGRAM_INDEX,
    NUMBER_OF_COINS,
    NUMBER_OF_TRIGRAMS,
    TRIGRAM_LENGTH,
)
from .errors import CoinTossError, TrigramError
from validators.coin_tosses import CoinTossesValidator


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

        self.present_schema = None
        self.present_index = None

        self.future_schema = None
        self.future_index = None

        CoinTossesValidator(coin_tosses)
        self.__prepare(coin_tosses)
        self.__validate()

    def __prepare(self, coin_tosses: list) -> None:
        self.coin_tosses = coin_tosses

        self.present_schema = '\n'.join((COIN_TOSS_TO_PRESENT_SCHEMA[toss] for toss in self.coin_tosses))
        present_line_index = tuple((COIN_TOSS_TO_PRESENT_INDEX[toss] for toss in self.coin_tosses))
        self.present_index = LINE_INDICES_TO_TRIGRAM_INDEX[present_line_index]

        self.future_schema = '\n'.join((COIN_TOSS_TO_FUTURE_SCHEMA[toss] for toss in self.coin_tosses))
        future_line_index = tuple((COIN_TOSS_TO_FUTURE_INDEX[toss] for toss in self.coin_tosses))
        self.future_index = LINE_INDICES_TO_TRIGRAM_INDEX[future_line_index]
    
    def validate(self) -> None:
        self.__validate()
    
    def __validate(self) -> None:
        if type(self.present_schema) is not str:
            raise TrigramError('The present Trigram schema is not a string.')
        if self.present_schema.count('\n') != TRIGRAM_LENGTH - 1:
            raise TrigramError('The present Trigram schema is incorrect. Try building the Trigram again.')
        if not 1 <= self.present_index <= NUMBER_OF_TRIGRAMS:
            raise TrigramError(f'The present Trigram has incorrect index {self.present_index}.')

        if type(self.future_schema) is not str:
            raise TrigramError('The future Trigram schema is not a string.')
        if self.future_schema.count('\n') != TRIGRAM_LENGTH - 1:
            raise TrigramError('The future Trigram schema is incorrect. Try building the Trigram again.')
        if not 1 <= self.future_index <= NUMBER_OF_TRIGRAMS:
            raise TrigramError(f'The future Trigram has incorrect index {self.future_index}.')
