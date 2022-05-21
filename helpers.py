from constants import HEXAGRAMS

def validateConfig():
    values = list(HEXAGRAMS.values())
    assert min(values) == 1
    assert max(values) == 64
    assert len(set(values)) == 64
    assert type(values[0]) is int
    assert len(set(type(v) for v in values)) == 1
