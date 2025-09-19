from pypp_python import Valu, dataclass


@dataclass
class OnlyHDataClass:
    field1: Valu(list[float])
    field2: Valu(dict[str, set[int]])
