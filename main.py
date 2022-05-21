from random import randint

from coin import Coin
from constants import (
    COIN_TOSS_TO_PRESENT_SCHEMA,
    TRIGRAM_INDICES_TO_HEXAGRAM_INDEX,
)
from helpers import validateCodeConfiguration
from hexagram import Hexagram
from trigram import Trigram

# TODO: Use the altered algorithm for coin tosses using 4 coins or different throw schemes
def getCoinTossesForHexagram():
    coins = [Coin() for _ in range(3)]

    tosses = []
    for i in range(6):
        input()
        print(f'Line {6 - i} ', end='')
        toss = tossCoins(coins)
        print(COIN_TOSS_TO_PRESENT_SCHEMA[toss])
        tosses.append(toss)
    del coins

    tosses.reverse()
    return tosses[3:], tosses[:3]

def tossCoins(coins: list[Coin]):
    values = []
    for coin in coins:
        coin.toss()
        values.append(coin.getValue())

    heads = values.count(1)
    tails = values.count(0)

    return (heads, tails)

def main():
    try:
        validateCodeConfiguration()
    except AssertionError:
        print('There is a problem with the code configuration. Exiting...')
        return

    input('Type your question here and press enter: ')
    print('\nNow cast 6 times by pressing enter:')
    
    lower_coin_tosses, upper_coin_tosses = getCoinTossesForHexagram()
    lower_trigram = Trigram(lower_coin_tosses)
    upper_trigram = Trigram(upper_coin_tosses)
    hexagram = Hexagram(lower_trigram, upper_trigram)

    print(f'\nPresent Hexagram:\n\n{hexagram.present_schema}\n')
    print(f'Future Hexagram:\n\n{hexagram.future_schema}\n')

    print(f'To read more, visit the following URLs:')
    print(f'\nPresent: {hexagram.present_url}')
    print(f'Future:  {hexagram.future_url}\n')

if __name__ == '__main__':
    main()
