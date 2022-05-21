from constants import (
    HEXAGRAM_LENGTH,
    NUMBER_OF_HEXAGRAMS,
    NUMBER_OF_TRIGRAMS,
    TRIGRAM_INDICES_TO_HEXAGRAM_INDEX,
    TRIGRAM_LENGTH,
)
from errors import TrigramError, HexagramError
from trigram import Trigram


class Hexagram:
    def __init__(self, lower: Trigram, upper: Trigram):
        self.lower = None
        self.upper = None

        self.present_schema = None
        self.present_index = None
        self.present_url = None

        self.future_schema = None
        self.future_index = None
        self.future_url = None

        self.__validateTrigram(lower)
        self.__validateTrigram(upper)

        self.__prepare(lower, upper)
        self.__validate()

    def __validateTrigram(self, trigram: Trigram):
        self.__validateTosses(trigram.coin_tosses)
        
        self.__validateSchema(trigram.present_schema)
        self.__validateIndex(trigram.present_index)

        self.__validateSchema(trigram.future_schema)
        self.__validateIndex(trigram.future_index)
    
    def __validateTosses(self, coin_tosses):
        if type(coin_tosses) != list:
            raise TrigramError('The Trigram has coin tosses that are not a list.')

        if len(coin_tosses) != TRIGRAM_LENGTH:
            raise TrigramError(f'The Trigram does not have {TRIGRAM_LENGTH} coin tosses.')
    
    def __validateSchema(self, schema):
        if type(schema) != str:
            raise TrigramError(f'The Trigram has incorrect format {repr(schema)}.') 

    def __validateIndex(self, index):
        if type(index) != int:
            raise TrigramError(f'The Trigram index {index} is of type {type(index)}. It must be an integer instead.')

        if index < 1 or index > NUMBER_OF_TRIGRAMS:
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
