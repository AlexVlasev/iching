import pytest

from errors import CoinTossError, TrigramError
from trigram import Trigram

def getFaultyTosses():
    return [
        'abc',
        [],
        ['a', 'b', 'c'],
        [(0, 0), (0, 3), (0, 3)],
        [('a', 3), (0, 3), (0, 3)],
    ]

@pytest.mark.parametrize("coin_tosses", getFaultyTosses())
def testInvalidCoinTosses(coin_tosses):
    with pytest.raises(CoinTossError):
        trigram = Trigram(coin_tosses)

def getFaultySchemas():
    return [
        None,
        1,
        'a',
        'a\nb',
    ]

@pytest.mark.parametrize("schema", getFaultySchemas())
def testInvalidSchema(schema):
    trigram = Trigram([(0, 3), (0, 3), (0, 3)])
    trigram.present_schema = schema
    with pytest.raises(TrigramError):
        trigram.validate()

def testHappyPath():
    coin_tosses = [(0, 3), (1, 2), (2, 1)]
    trigram = Trigram(coin_tosses)
