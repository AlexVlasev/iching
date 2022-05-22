import pytest

from src.errors import CoinTossError, SchemaError
from src.trigram import Trigram


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
    with pytest.raises(CoinTossError):
        Trigram(coin_tosses)

def get_faulty_schemas():
    return [
        None,
        1,
        'a',
        'a\nb',
    ]

@pytest.mark.parametrize("schema", get_faulty_schemas())
def test_invalid_schema(schema):
    trigram = Trigram([(0, 3), (0, 3), (0, 3)])
    trigram.schemas['present'] = schema
    with pytest.raises(SchemaError):
        trigram.validate()

def test_happy_path():
    coin_tosses = [(0, 3), (1, 2), (2, 1)]
    Trigram(coin_tosses)
