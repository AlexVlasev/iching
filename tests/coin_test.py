import pytest

from src.coin import Coin
from src.errors import CoinTossError

def invalid_coin_states():
    return [
        (None, True),
        (None, 1),
        (0, 'abc'),
        (1, False),
        ('1', True),
        (2, True),
    ]

@pytest.mark.parametrize("value,tossed", invalid_coin_states())
def test_cannot_toss(value, tossed):
    coin = Coin()
    coin.value = value
    coin.tossed = tossed
    with pytest.raises(CoinTossError):
        coin.toss()

@pytest.mark.parametrize("value,tossed", invalid_coin_states())
def test_cannot_get_value(value, tossed):
    coin = Coin()
    coin.value = value
    coin.tossed = tossed
    with pytest.raises(CoinTossError):
        value = coin.get_value()

def coin_is_reset(coin):
    assert coin.value is None
    assert coin.tossed is False

def coin_is_tossed(coin):
    assert coin.value is not None
    assert coin.tossed

def test_happy_path():
    coin = Coin()
    coin_is_reset(coin)

    coin.toss()
    coin_is_tossed(coin)

    coin.get_value()
    coin_is_reset(coin)
