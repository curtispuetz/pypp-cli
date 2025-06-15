from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True, slots=True)
class AngInc:
    # Angle Bracket Include
    val: str


@dataclass(frozen=True, slots=True)
class QInc:
    # Quotes Include
    val: str


CppInclude = Union[AngInc, QInc]

HAndCppParts = tuple[list[str], list[str]]
