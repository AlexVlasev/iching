from src.constants import (
    NUMBER_OF_COINS,
    TRIGRAM_LENGTH,
)
from src.errors import CoinTossError

class CoinTossesValidator:
    def __init__(self, coin_tosses: list):
        self.__validateCoinTosses(coin_tosses)

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