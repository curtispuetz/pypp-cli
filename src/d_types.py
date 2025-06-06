from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True, slots=True)
class SBInc:
    # Square Bracket Include
    val: str


@dataclass(frozen=True, slots=True)
class QInc:
    # Quotes Include
    val: str


CppInclude = Union[SBInc, QInc]

HAndCppParts = tuple[list[str], list[str]]
