from random import randint

from errors import CoinTossError


class Coin:
    """
    The Coin class provides an API for obtaining a random value with a number
    of checks and validations along the way.
    
    The usage is strict. Once a Coin is instantiated, the user has to toss it
    before obtaining its value. Once a value is obtained, the coin can
    be tossed once again. An action (toss, getValue) cannot be performed
    twice in a row.

    The validation is there to assure there is no tampering with the Coin.
    """
    def __init__(self):
        self.__resetCoin()
    
    def __resetCoin(self):
        self.value = None
        self.tossed = False
        self.__validate()

    def __validate(self):
        if self.value is not None and type(self.value) is not int and self.value not in [0, 1]:
            raise CoinTossError(f'Coin has incorrect value {self.value}. Only 0 or 1 are allowed.')
        if type(self.tossed) is not bool:
            raise CoinTossError(f'Coin has incorrect toss status {self.tossed}. Only False and True are allowed.')

        if self.value is None and self.tossed:
            raise CoinTossError('Coin has no value, but appears to have been tossed.')
        if self.value and not self.tossed:
            raise CoinTossError(f'Coin has value {self.value}, but it has not been tossed.')
    
    def toss(self):
        self.__validate()
        if self.value or self.tossed:
            raise CoinTossError('Cannot toss coin before value is obtained. Please use a new coin or reset.')
        self.value = randint(0, 1)
        self.tossed = True
        self.__validate()
    
    def getValue(self):
        self.__validate()
        if self.value is None or not self.tossed:
            raise CoinTossError('Cannot obtain value from coin that is not tossed yet.')

        value = self.value
        self.__resetCoin()

        return value
