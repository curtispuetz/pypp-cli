from dataclasses import dataclass

from test_dir.python.pypp.ownership import Valu


@dataclass
class OnlyHDataClass:
    field1: Valu(list[float])
    field2: Valu(dict[str, set[int]])
