from dataclasses import dataclass

from pypp_core.src.d_types import PySpecificImport, CppInclude


@dataclass(frozen=True, slots=True)
class MapInfo:
    val: str
    includes: list[CppInclude]
    required_import: PySpecificImport | None = None


@dataclass(frozen=True, slots=True)
class CallMapInfo:
    left: str
    right: str
    includes: list[CppInclude]
    required_import: PySpecificImport | None = None


type NamesMap = dict[str, MapInfo]
type CallsMap = dict[str, CallMapInfo]
type AttrsMap = dict[str, MapInfo]
type FnArgsByValueMap = dict[str, PySpecificImport | None]
type SubscriptableTypesMap = dict[str, PySpecificImport | None]

type NamesCallsOrAttrsMap = NamesMap | CallsMap | AttrsMap
type NamesCallsOrAttrsMapInfo = MapInfo | CallMapInfo
