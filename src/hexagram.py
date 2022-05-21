from .constants import (
    HEXAGRAM_LENGTH,
    NUMBER_OF_COINS,
    NUMBER_OF_HEXAGRAMS,
    NUMBER_OF_TRIGRAMS,
    TRIGRAM_INDICES_TO_HEXAGRAM_INDEX,
    TRIGRAM_LENGTH,
)
from .errors import (
    CoinTossError,
    HexagramError,
    TrigramError,
)
from .trigram import Trigram
from validators.coin_tosses import CoinTossesValidator


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

    def __validateTrigram(self, trigram: Trigram) -> None:
        if not isinstance(trigram, Trigram):
            raise TrigramError('Invalid Trigram object provided to Hexagram.')

        CoinTossesValidator(trigram.coin_tosses)
        
        self.__validateTrigramSchema(trigram.present_schema)
        self.__validateTrigramIndex(trigram.present_index)

        self.__validateTrigramSchema(trigram.future_schema)
        self.__validateTrigramIndex(trigram.future_index)

    def __validateTrigramSchema(self, schema: str) -> None:
        if type(schema) != str:
            raise TrigramError(f'The Trigram has incorrect format {repr(schema)}.') 

    def __validateTrigramIndex(self, index: int) -> None:
        if type(index) != int:
            raise TrigramError(f'The Trigram index {index} is of type {type(index)}. It must be an integer instead.')

        if not 1 <= index <= NUMBER_OF_TRIGRAMS:
            raise TrigramError(f'The Trigram index {index} is incorrect. It must be between 1 and {NUMBER_OF_TRIGRAMS} included.')

    def __prepare(self, lower_trigram: Trigram, upper_trigram: Trigram) -> None:
        self.lower_trigram = lower_trigram
        self.upper_trigram = upper_trigram

        self.present_schema = '\n'.join([self.upper_trigram.present_schema, self.lower_trigram.present_schema])
        self.present_index = TRIGRAM_INDICES_TO_HEXAGRAM_INDEX[(lower_trigram.present_index, upper_trigram.present_index)]
        self.present_url = f'https://divination.com/iching/lookup/{self.present_index}-2'

        self.future_schema = '\n'.join([self.upper_trigram.future_schema, self.lower_trigram.future_schema])
        self.future_index = TRIGRAM_INDICES_TO_HEXAGRAM_INDEX[(lower_trigram.future_index, upper_trigram.future_index)]
        self.future_url = f'https://divination.com/iching/lookup/{self.future_index}-2'
    
    def validate(self) -> None:
        self.__validate()
    
    def __validate(self) -> None:
        if type(self.present_schema) is not str:
            raise HexagramError('The present Hexagram schema must be a string.')
        if self.present_schema.count('\n') != HEXAGRAM_LENGTH - 1:
            raise HexagramError('The present Hexagram schema is incorrect. Try building the Hexagram again.')

        if not 1 <= self.present_index <= NUMBER_OF_HEXAGRAMS:
            raise HexagramError(f'The present Hexagram has incorrect index {self.present_index}.')

        if type(self.future_schema) is not str:
            raise HexagramError('The future Hexagram schema must be a string.')
        if self.future_schema.count('\n') != HEXAGRAM_LENGTH - 1:
            raise HexagramError('The future Hexagram schema is incorrect. Try building the Hexagram again.')
        
        if not 1 <= self.future_index <= NUMBER_OF_HEXAGRAMS:
            raise HexagramError(f'The future Hexagram has incorrect index {self.future_index}.')
