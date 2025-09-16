from dataclasses import dataclass

from pypp_python import Valu


@dataclass
class OnlyHDataClass:
    field1: Valu(list[float])
    field2: Valu(dict[str, set[int]])
