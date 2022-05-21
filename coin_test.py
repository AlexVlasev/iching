import pytest

from coin import Coin
from errors import CoinTossError

def invalidCoinStates():
    return [
        (None, True),
        (None, 1),
        (0, 'abc'),
        (1, False),
        ('1', True),
        (2, True),
    ]

@pytest.mark.parametrize("value,tossed", invalidCoinStates())
def testCannotToss(value, tossed):
    coin = Coin()
    coin.value = value
    coin.tossed = tossed
    with pytest.raises(CoinTossError):
        coin.toss()

@pytest.mark.parametrize("value,tossed", invalidCoinStates())
def testCannotGetValue(value, tossed):
    coin = Coin()
    coin.value = value
    coin.tossed = tossed
    with pytest.raises(CoinTossError):
        value = coin.getValue()

def coinIsReset(coin):
    assert coin.value is None
    assert coin.tossed is False

def coinIsTossed(coin):
    assert coin.value is not None
    assert coin.tossed

def testHappyPath():
    coin = Coin()
    coinIsReset(coin)

    coin.toss()
    coinIsTossed(coin)

    value = coin.getValue()
    coinIsReset(coin)