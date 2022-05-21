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
    def __init__(self, coin_tosses: list):
        self.coin_tosses = None

        self.present_schema = None
        self.present_index = None

        self.future_schema = None
        self.future_index = None

        self.__validateCoinTosses(coin_tosses)
        self.__prepare(coin_tosses)
        self.__validate()

    def __validateCoinTosses(self, coin_tosses: list):
        if type(coin_tosses) != list:
            raise TrigramError('The Trigram has coin tosses that are not a list.')

        if len(coin_tosses) != TRIGRAM_LENGTH:
            raise TrigramError(f'The Trigram does not have {TRIGRAM_LENGTH} coin tosses.')

        for toss in coin_tosses:
            heads, tails = toss
            self.__validateCoinTossPart(heads, 'heads')
            self.__validateCoinTossPart(tails, 'tails')
            if heads + tails != NUMBER_OF_COINS:
                raise CoinTossError(f'The total number of throws must equal {NUMBER_OF_COINS}. Got {heads + tails} instead.')

    def __validateCoinTossPart(self, coin_toss_part: tuple, toss_type):
        if type(coin_toss_part) != int:
            raise CoinTossError(f'The number of {toss_type} needs to be an integer.')
        if not 0 <= coin_toss_part <= NUMBER_OF_COINS:
            raise CoinTossError(f'The number of {toss_type} must be between 0 and {NUMBER_OF_COINS} included.')

    def __prepare(self, coin_tosses: list):
        self.coin_tosses = coin_tosses

        self.present_schema = '\n'.join((COIN_TOSS_TO_PRESENT_SCHEMA[toss] for toss in self.coin_tosses))
        present_line_index = tuple((COIN_TOSS_TO_PRESENT_INDEX[toss] for toss in self.coin_tosses))
        self.present_index = LINE_INDICES_TO_TRIGRAM_INDEX[present_line_index]

        self.future_schema = '\n'.join((COIN_TOSS_TO_FUTURE_SCHEMA[toss] for toss in self.coin_tosses))
        future_line_index = tuple((COIN_TOSS_TO_FUTURE_INDEX[toss] for toss in self.coin_tosses))
        self.future_index = LINE_INDICES_TO_TRIGRAM_INDEX[future_line_index]
    
    def __validate(self):
        if self.present_schema.count('\n') != TRIGRAM_LENGTH - 1:
            raise TrigramError('The Trigram present schema is incorrect. Try building the Trigram again.')
        if not 1 <= self.present_index <= NUMBER_OF_TRIGRAMS:
            raise TrigramError(f'The Trigram has incorrect index {self.present_index}.')

        if self.future_schema.count('\n') != TRIGRAM_LENGTH - 1:
            raise TrigramError('The Trigram present schema is incorrect. Try building the Trigram again.')
        if not 1 <= self.future_index <= NUMBER_OF_TRIGRAMS:
            raise TrigramError(f'The Trigram has incorrect index {self.future_index}.')
