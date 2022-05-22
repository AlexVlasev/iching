from src.coin import Coin
from src.constants import COIN_TOSS_TO_PRESENT_SCHEMA
from src.helpers import validate_code_configuration
from src.hexagram import Hexagram
from src.trigram import Trigram


# TODO: Use the altered algorithm for coin tosses using 4 coins or different throw schemes
def get_coin_tosses_for_hexagram():
    coins = [Coin() for _ in range(3)]

    tosses = []
    for i in range(6):
        input()
        print(f'Line {6 - i} ', end='')
        toss = toss_coins(coins)
        print(COIN_TOSS_TO_PRESENT_SCHEMA[toss])
        tosses.append(toss)
    del coins

    tosses.reverse()
    return tosses[3:], tosses[:3]

def toss_coins(coins: list[Coin]):
    values = []
    for coin in coins:
        coin.toss()
        values.append(coin.get_value())

    heads = values.count(1)
    tails = values.count(0)

    return (heads, tails)

def main():
    try:
        validate_code_configuration()
    except AssertionError:
        print('There is a problem with the code configuration. Exiting...')
        return

    input('Type your question here and press enter: ')
    print('\nNow cast 6 times by pressing enter:')

    lower_coin_tosses, upper_coin_tosses = get_coin_tosses_for_hexagram()
    lower_trigram = Trigram(lower_coin_tosses)
    upper_trigram = Trigram(upper_coin_tosses)
    hexagram = Hexagram(lower_trigram, upper_trigram)

    present_schema = hexagram.schemas['present']
    future_schema = hexagram.schemas['future']
    print(f'\nPresent Hexagram:\n\n{present_schema.schema}\n')
    print(f'Future Hexagram:\n\n{future_schema.schema}\n')

    print('To read more, visit the following URLs:')
    print(f'\nPresent: {present_schema.url}')
    print(f'Future:  {future_schema.url}\n')

if __name__ == '__main__':
    main()
