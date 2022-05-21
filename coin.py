from random import randint
from errors import TossException


class Coin:
    def __init__(self):
        self.__resetCoin()
    
    def __resetCoin(self):
        self.value = None
        self.tossed = False
        self.__validate()

    def __validate(self):
        if self.value is None and self.tossed:
            raise TossException('Coin has no value, but appears to have been tossed.')
        if self.value and not self.tossed:
            raise TossException(f'Coin has value {self.value}, but it has not been tossed.')
        if self.value and self.value not in [0, 1]:
            raise TossException(f'Coin has incorrect value {self.value}. Only 0 or 1 are allowed.')
    
    def toss(self):
        if self.value or self.tossed:
            raise TossException('The coin was not tossed properly. Please use a new coin or reset.')
        self.value = randint(0, 1)
        self.tossed = True
        self.__validate()
    
    def getValue(self):
        if self.value is None or not self.tossed:
            raise TossException('Cannot obtain value from coin that is not tossed yet.')

        value = self.value
        self.__resetCoin()

        return value
