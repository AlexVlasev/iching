from constants import (
    COIN_TOSS_TO_FUTURE_INDEX,
    COIN_TOSS_TO_FUTURE_SCHEMA,
    COIN_TOSS_TO_PRESENT_INDEX,
    COIN_TOSS_TO_PRESENT_SCHEMA,
    LINE_INDICES_TO_TRIGRAM_INDEX,
    NUMBER_OF_COINS,
    NUMBER_OF_TRIGRAMS,
    TRIGRAM_LENGTH,
)
from errors import CoinTossError, TrigramError


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

        self.__validateCoinTosses(coin_tosses)
        self.__prepare(coin_tosses)
        self.__validate()

    def __validateCoinTosses(self, coin_tosses: list) -> None:
        if type(coin_tosses) != list:
            raise CoinTossError('The Trigram has coin tosses that are not a list.')

        if len(coin_tosses) != TRIGRAM_LENGTH:
            raise CoinTossError(f'The Trigram does not have {TRIGRAM_LENGTH} coin tosses.')

        for coin_toss in coin_tosses:
            self.__validateCoinToss(coin_toss)

    def __validateCoinToss(self, coin_toss: tuple) -> None:
        if type(coin_toss) is not tuple:
            raise CoinTossError(f'The provided coin toss is not a tuple')
        if len(coin_toss) != 2:
            raise CoinTossError(f'The provided coin toss does not have two entries')

        heads, tails = coin_toss
        self.__validateCoinTossPart(heads, 'heads')
        self.__validateCoinTossPart(tails, 'tails')
        if heads + tails != NUMBER_OF_COINS:
            raise CoinTossError(f'The total number of throws must equal {NUMBER_OF_COINS}. Got {heads + tails} instead.')

    def __validateCoinTossPart(self, coin_toss_part: int, toss_type: str) -> None:
        if type(coin_toss_part) != int:
            raise CoinTossError(f'The number of {toss_type} needs to be an integer.')
        if not 0 <= coin_toss_part <= NUMBER_OF_COINS:
            raise CoinTossError(f'The number of {toss_type} must be between 0 and {NUMBER_OF_COINS} included.')

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
