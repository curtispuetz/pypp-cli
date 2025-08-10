from dataclasses import dataclass

from pypp_core.src.d_types import PySpecificImport, CppInclude


@dataclass(frozen=True, slots=True)
class MapInfo:
    val: str
    includes: list[CppInclude]
    required_import: PySpecificImport | None = None
