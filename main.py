from random import randint

from coin import Coin
from constants import HEXAGRAMS, P_MAP
from helpers import validateConfig
from hexagram import Hexagram
from trigram import Trigram

def getTossesForHexagram():
    coins = [Coin() for _ in range(3)]

    tosses = []
    for i in range(6):
        input()
        print(f'Line {6 - i} ', end='')
        toss = tossCoins(coins)
        print(P_MAP[toss])
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
    validateConfig()

    input('Type your question here and press enter: ')
    print('\nNow cast 6 times by pressing enter:')
    
    lower_tosses, upper_tosses = getTossesForHexagram()
    lower = Trigram(lower_tosses)
    upper = Trigram(upper_tosses)
    hexagram = Hexagram(lower, upper)

    print(f'\nPresent Hexagram:\n\n{hexagram.present_schema}\n')
    print(f'Future Hexagram:\n\n{hexagram.future_schema}\n')

    print(f'To read more, visit the following URLs:')
    print(f'\nPresent: {hexagram.present_url}')
    print(f'Future:  {hexagram.future_url}\n')

if __name__ == '__main__':
    main()
