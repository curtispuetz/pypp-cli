from collections.abc import Callable
from dataclasses import dataclass

from pypp_core.src.d_types import PySpecificImport, CppInclude


@dataclass(frozen=True, slots=True)
class MapInfo:
    val: str
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class CallMapInfoLeftAndRight:
    left: str
    right: str
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class CallMapInfoCppCall:
    cpp_call: str
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class CallMapInfoCustomMapping:
    mapping_fn: Callable
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class CallMapInfoCustomMappingFromLibrary:
    mapping_fn_str: str
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class CallMapInfoCustomMappingStartsWith:
    mapping_fn: Callable
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class CallMapInfoCustomMappingStartsWithFromLibrary:
    mapping_fn_str: str
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class CallMapInfoReplaceDotWithDoubleColon:
    includes: list[CppInclude]


type CallMapInfo = (
    CallMapInfoLeftAndRight
    | CallMapInfoCppCall
    | CallMapInfoCustomMapping
    | CallMapInfoCustomMappingFromLibrary
    | CallMapInfoCustomMappingStartsWith
    | CallMapInfoCustomMappingStartsWithFromLibrary
    | CallMapInfoReplaceDotWithDoubleColon
)

type NamesMapValue = dict[PySpecificImport | None, MapInfo]
type CallsMapValue = dict[PySpecificImport | None, CallMapInfo]
type AttrsMapValue = dict[PySpecificImport | None, MapInfo]
type FnArgsByValueMapValue = dict[PySpecificImport | None, None]
type SubscriptableTypesMapValue = dict[PySpecificImport | None, None]
type NamesMap = dict[str, NamesMapValue]
type CallsMap = dict[str, CallsMapValue]
type AttrsMap = dict[str, AttrsMapValue]
type FnArgsByValueMap = dict[str, FnArgsByValueMapValue]
type SubscriptableTypesMap = dict[str, SubscriptableTypesMapValue]

type NamesOrAttrsMap = NamesMap | AttrsMap
type NamesCallsOrAttrsMapValue = NamesMapValue | AttrsMapValue | CallsMapValue
