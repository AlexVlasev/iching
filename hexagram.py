from constants import (
    HEXAGRAM_LENGTH,
    NUMBER_OF_COINS,
    NUMBER_OF_HEXAGRAMS,
    NUMBER_OF_TRIGRAMS,
    TRIGRAM_INDICES_TO_HEXAGRAM_INDEX,
    TRIGRAM_LENGTH,
)
from errors import (
    CoinTossError,
    HexagramError,
    TrigramError,
)
from trigram import Trigram


class Hexagram:
    """
    The Hexagram class provides a simple API to convert two Trigrams
    into a Hexagram. There are a number of checks and validations along the way.

    Once the Trigrams are validated, a Hexagram is constructed. Then a user
    can obtain its schema and/or index directly.

    TODO: create getters for the schema and for the index.
    """
    def __init__(self, lower_trigram: Trigram, upper_trigram: Trigram):
        self.lower = None
        self.upper = None

        self.present_schema = None
        self.present_index = None
        self.present_url = None

        self.future_schema = None
        self.future_index = None
        self.future_url = None

        self.__validateTrigram(lower_trigram)
        self.__validateTrigram(upper_trigram)

        self.__prepare(lower_trigram, upper_trigram)
        self.__validate()

    def __validateTrigram(self, trigram: Trigram):
        if not isinstance(trigram, Trigram):
            raise TrigramError('Invalid Trigram object provided to Hexagram.')

        self.__validateCoinTosses(trigram.coin_tosses)
        
        self.__validateTrigramSchema(trigram.present_schema)
        self.__validateTrigramIndex(trigram.present_index)

        self.__validateTrigramSchema(trigram.future_schema)
        self.__validateTrigramIndex(trigram.future_index)
    
    def __validateCoinTosses(self, coin_tosses):
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

    def __validateTrigramSchema(self, schema):
        if type(schema) != str:
            raise TrigramError(f'The Trigram has incorrect format {repr(schema)}.') 

    def __validateTrigramIndex(self, index):
        if type(index) != int:
            raise TrigramError(f'The Trigram index {index} is of type {type(index)}. It must be an integer instead.')

        if not 1 <= index <= NUMBER_OF_TRIGRAMS:
            raise TrigramError(f'The Trigram index {index} is incorrect. It must be between 1 and {NUMBER_OF_TRIGRAMS} included.')

    def __prepare(self, lower: Trigram, upper: Trigram):
        self.lower = lower
        self.upper = upper

        self.present_schema = '\n'.join([self.upper.present_schema, self.lower.present_schema])
        self.present_index = TRIGRAM_INDICES_TO_HEXAGRAM_INDEX[(lower.present_index, upper.present_index)]
        self.present_url = f'https://divination.com/iching/lookup/{self.present_index}-2'

        self.future_schema = '\n'.join([self.upper.future_schema, self.lower.future_schema])
        self.future_index = TRIGRAM_INDICES_TO_HEXAGRAM_INDEX[(lower.future_index, upper.future_index)]
        self.future_url = f'https://divination.com/iching/lookup/{self.future_index}-2'
    
    def __validate(self):
        if self.present_schema.count('\n') != HEXAGRAM_LENGTH - 1:
            raise HexagramError()('The Hexagram present schema is incorrect. Try building the Trigram again.')
        if not 1 <= self.present_index <= NUMBER_OF_HEXAGRAMS:
            raise HexagramError(f'The Hexagram has incorrect index {self.present_index}.')

        if self.future_schema.count('\n') != HEXAGRAM_LENGTH - 1:
            raise HexagramError('The Hexagram present schema is incorrect. Try building the Trigram again.')
        if not 1 <= self.future_index <= NUMBER_OF_HEXAGRAMS:
            raise HexagramError(f'The Hexagram has incorrect index {self.future_index}.')
