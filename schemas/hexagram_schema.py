from src.constants import TRIGRAM_INDICES_TO_HEXAGRAM_INDEX
from src.errors import SchemaError, TrigramError
from src.trigram import Trigram
from validators.hexagram_schema import HexagramSchemaValidator


class HexagramSchema:
    """
    The Hexagram Schema class helps in constructing and validating a hexagram.
    """
    def __init__(
        self,
        lower_trigram: Trigram,
        upper_trigram: Trigram,
        schema_type: str,
        validate_trigrams: bool
    ):
        if validate_trigrams:
            if isinstance(lower_trigram, Trigram):
                raise TrigramError('Provided lower Trigram is not a Trigram')
            lower_trigram.validate()

            if isinstance(upper_trigram, Trigram):
                raise TrigramError('Provided upper Trigram is not a Trigram')
            upper_trigram.validate()

        if schema_type not in ['present', 'future']:
            raise SchemaError(f'The provided schema has invalid type {schema_type}')
        self.schema_type = schema_type

        self.schema = None
        self.index = None
        self.url = None
        self.__prepare(lower_trigram, upper_trigram)

        HexagramSchemaValidator(self.schema, self.index, self.schema_type)

    def __prepare(self, lower_trigram: Trigram, upper_trigram: Trigram) -> None:
        lower_schema = lower_trigram.schemas[self.schema_type]
        upper_schema = upper_trigram.schemas[self.schema_type]
        self.schema = '\n'.join([upper_schema.schema, lower_schema.schema])
        self.index = TRIGRAM_INDICES_TO_HEXAGRAM_INDEX[(lower_schema.index, upper_schema.index)]
        self.url = f'https://divination.com/iching/lookup/{self.index}-2'
