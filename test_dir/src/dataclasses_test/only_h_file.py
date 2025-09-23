from pypp_python import Val, dataclass


@dataclass
class OnlyHDataClass:
    field1: Val[list[float]]
    field2: Val[dict[str, set[int]]]
