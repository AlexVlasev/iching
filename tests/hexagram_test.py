import pytest

from src.errors import CoinTossError, HexagramError
from src.hexagram import Trigram, Hexagram

def get_faulty_tosses():
    return [
        'abc',
        [],
        ['a', 'b', 'c'],
        [(0, 0), (0, 3), (0, 3)],
        [('a', 3), (0, 3), (0, 3)],
    ]

@pytest.mark.parametrize("coin_tosses", get_faulty_tosses())
def test_invalid_coin_tosses(coin_tosses):
    lower_trigram = Trigram([(1,2), (1,2), (1,2)])
    upper_trigram = Trigram([(1,2), (1,2), (1,2)])
    with pytest.raises(CoinTossError):
        lower_trigram.coin_tosses = coin_tosses
        Hexagram(lower_trigram, upper_trigram)

def get_faulty_schemas():
    return [
        None,
        1,
        'a',
        'a\nb',
    ]

@pytest.mark.parametrize("schema", get_faulty_schemas())
def test_invalid_schema(schema):
    lower_trigram = Trigram([(0, 3), (0, 3), (0, 3)])
    upper_trigram = Trigram([(0, 3), (0, 3), (0, 3)])
    hexagram = Hexagram(lower_trigram, upper_trigram)
    hexagram.present_schema = schema
    with pytest.raises(HexagramError):
        hexagram.validate()

def test_happy_path():
    lower_coin_tosses = [(0, 3), (1, 2), (2, 1)]
    lower_trigram = Trigram(lower_coin_tosses)
    upper_coin_tosses = [(1, 2), (2, 1), (3, 0)]
    upper_trigram = Trigram(upper_coin_tosses)
    Hexagram(lower_trigram, upper_trigram)
