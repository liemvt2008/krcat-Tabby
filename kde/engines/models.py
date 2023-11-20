import typing
from dataclasses import asdict, dataclass, field

UNKNOWN_VALUE_NUM = -1
UNKNOWN_VALUE_STR = 'unknown'


@dataclass
class EngineResult:
    value: typing.Union[int, float, list, str] = field()

    probability: float = field(default=1.)

    engine_name: typing.Union[str, None] = field(default=None)

    properties: typing.Union[dict, None] = field(default=None)

    def to_dict(self):
        return asdict(self)
