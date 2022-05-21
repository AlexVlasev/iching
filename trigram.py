from errors import TossException
from constants import F_LINE_MAP, F_MAP, P_LINE_MAP, P_MAP, TRIGRAMS


class Trigram:
    def __init__(self, tosses: list):
        self.tosses = None
        self.present_schema = None
        self.present_index = None
        self.future_schema = None
        self.future_index = None

        self.__validate(tosses)
        self.__prepare(tosses)

    def __validate(self, tosses: list):
        for toss in tosses:
            heads, tails = toss
            self.__validateTossPart(heads)
            self.__validateTossPart(tails)
            if heads + tails != 3:
                raise TossException(f'The total number of throws must equal 3. Got {heads + tails} instead.')

    def __validateTossPart(self, toss_part: tuple):
        if type(toss_part) != int:
            raise TossException('The toss part needs to be an integer.')
        if toss_part < 0 or toss_part > 3:
            raise TossException('The toss must be between 0 and 3 included.')

    def __prepare(self, tosses: list):
        self.tosses = tosses

        self.present_schema = '\n'.join((P_MAP[toss] for toss in self.tosses))
        present_line_index = tuple((P_LINE_MAP[toss] for toss in self.tosses))
        self.present_index = TRIGRAMS[present_line_index]

        self.future_schema = '\n'.join((F_MAP[toss] for toss in self.tosses))
        future_line_index = tuple((F_LINE_MAP[toss] for toss in self.tosses))
        self.future_index = TRIGRAMS[future_line_index]
