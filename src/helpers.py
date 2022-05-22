from .constants import (
    NUMBER_OF_HEXAGRAMS,
    TRIGRAM_INDICES_TO_HEXAGRAM_INDEX,
)

# TODO: Add validation for trigram indices
# TODO: Add validation for hexagram indices made out of trigrams
def validate_code_configuration():
    values = list(TRIGRAM_INDICES_TO_HEXAGRAM_INDEX.values())
    assert min(values) == 1
    assert max(values) == NUMBER_OF_HEXAGRAMS
    assert len(set(values)) == NUMBER_OF_HEXAGRAMS
    assert isinstance(values[0], int)
    assert len(set(type(v) for v in values)) == 1
