from errors import TrigramError
from constants import HEXAGRAMS
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

    def __validateTrigram(self, trigram: Trigram):
        self.__validateTosses(trigram.tosses)
        
        self.__validateSchema(trigram.present_schema)
        self.__validateIndex(trigram.present_index)

        self.__validateSchema(trigram.future_schema)
        self.__validateIndex(trigram.future_index)
    
    def __validateTosses(self, tosses):
        if type(tosses) != list:
            raise TrigramError('The trigram has tosses that are not a list.')

        if len(tosses) != 3:
            raise TrigramError('The trigram does not have 3 tosses.')
    
    def __validateSchema(self, schema):
        if type(schema) != str:
            raise TrigramError(f'The trigram has incorrect format {repr(schema)}.') 

    def __validateIndex(self, index):
        if type(index) != int:
            raise TrigramError(f'The index {index} of the trigram is not an integer.')

        if index < 1 or index > 8:
            raise TrigramError(f'The index {index} is incorrect.')

    def __prepare(self, lower: Trigram, upper: Trigram):
        self.lower = lower
        self.upper = upper

        self.present_schema = '\n'.join([self.upper.present_schema, self.lower.present_schema])
        self.present_index = HEXAGRAMS[(lower.present_index, upper.present_index)]
        self.present_url = f'https://divination.com/iching/lookup/{self.present_index}-2'

        self.future_schema = '\n'.join([self.upper.future_schema, self.lower.future_schema])
        self.future_index = HEXAGRAMS[(lower.future_index, upper.future_index)]
        self.future_url = f'https://divination.com/iching/lookup/{self.future_index}-2'
