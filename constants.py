NUMBER_OF_COINS = 3

TRIGRAM_LENGTH = 3
NUMBER_OF_TRIGRAMS = 8

HEXAGRAM_LENGTH = 6
NUMBER_OF_HEXAGRAMS = 64

COIN_TOSS_TO_PRESENT_SCHEMA = {
    (3, 0): '-o-',
    (2, 1): '- -',
    (1, 2): '---',
    (0, 3): '-x-',
}

COIN_TOSS_TO_FUTURE_SCHEMA = {
    (3, 0): '- -',
    (2, 1): '- -',
    (1, 2): '---',
    (0, 3): '---',
}

COIN_TOSS_TO_PRESENT_INDEX = {
    (3, 0): 1,
    (2, 1): 0,
    (1, 2): 1,
    (0, 3): 0,
}

COIN_TOSS_TO_FUTURE_INDEX = {
    (3, 0): 0,
    (2, 1): 0,
    (1, 2): 1,
    (0, 3): 1,
}

# TODO: Convert to binary representation so these can be validated.
LINE_INDICES_TO_TRIGRAM_INDEX = {
    (1, 1, 1): 1,
    (0, 0, 1): 2,
    (0, 1, 0): 3,
    (1, 0, 0): 4,
    (0, 0, 0): 5,
    (1, 1, 0): 6,
    (1, 0, 1): 7,
    (0, 1, 1): 8,
}

# TODO: Convert to binary representation so these can be validated.
# TODO: Add a map from binary representation to actual hexagram indices.
# TODO: Add names so that other websites can be consulted.
TRIGRAM_INDICES_TO_HEXAGRAM_INDEX = {
    (1, 1): 1,
    (1, 2): 34,
    (1, 3): 5,
    (1, 4): 26,
    (1, 5): 11,
    (1, 6): 9,
    (1, 7): 14,
    (1, 8): 43,
    (2, 1): 25,
    (2, 2): 51,
    (2, 3): 3,
    (2, 4): 27,
    (2, 5): 24,
    (2, 6): 42,
    (2, 7): 21,
    (2, 8): 17,
    (3, 1): 6,
    (3, 2): 40,
    (3, 3): 29,
    (3, 4): 4,
    (3, 5): 7,
    (3, 6): 59,
    (3, 7): 64,
    (3, 8): 47,
    (4, 1): 33,
    (4, 2): 62,
    (4, 3): 39,
    (4, 4): 52,
    (4, 5): 15,
    (4, 6): 53,
    (4, 7): 56,
    (4, 8): 31,
    (5, 1): 12,
    (5, 2): 16,
    (5, 3): 8,
    (5, 4): 23,
    (5, 5): 2,
    (5, 6): 20,
    (5, 7): 35,
    (5, 8): 45,
    (6, 1): 44,
    (6, 2): 32,
    (6, 3): 48,
    (6, 4): 18,
    (6, 5): 46,
    (6, 6): 57,
    (6, 7): 50,
    (6, 8): 28,
    (7, 1): 13,
    (7, 2): 55,
    (7, 3): 63,
    (7, 4): 22,
    (7, 5): 36,
    (7, 6): 37,
    (7, 7): 30,
    (7, 8): 49,
    (8, 1): 10,
    (8, 2): 54,
    (8, 3): 60,
    (8, 4): 41,
    (8, 5): 19,
    (8, 6): 61,
    (8, 7): 38,
    (8, 8): 58,
}
