from collections.abc import Callable
from dataclasses import dataclass

from pypp_core.src.d_types import PySpecificImport, CppInclude


@dataclass(frozen=True, slots=True)
class MapInfo:
    val: str
    includes: list[CppInclude]
    required_import: PySpecificImport | None = None


@dataclass(frozen=True, slots=True)
class CallMapInfoLeftAndRight:
    left: str
    right: str
    includes: list[CppInclude]
    required_import: PySpecificImport | None = None


@dataclass(frozen=True, slots=True)
class CallMapInfoCppType:
    cpp_call: str
    includes: list[CppInclude]
    required_import: PySpecificImport | None = None


@dataclass(frozen=True, slots=True)
class CallMapInfoNone:
    includes: list[CppInclude]
    required_import: PySpecificImport | None = None


@dataclass(frozen=True, slots=True)
class CallMapInfoCustomMapping:
    mapping_fn: Callable
    includes: list[CppInclude]
    required_import: PySpecificImport | None = None


@dataclass(frozen=True, slots=True)
class CallMapInfoCustomMappingFromLibrary:
    mapping_fn_str: str
    includes: list[CppInclude]
    required_import: PySpecificImport | None = None


@dataclass(frozen=True, slots=True)
class CallMapInfoCustomMappingStartsWith:
    mapping_fn: Callable
    includes: list[CppInclude]
    required_import: PySpecificImport | None = None


@dataclass(frozen=True, slots=True)
class CallMapInfoCustomMappingStartsWithFromLibrary:
    mapping_fn_str: str
    includes: list[CppInclude]
    required_import: PySpecificImport | None = None


@dataclass(frozen=True, slots=True)
class CallMapInfoReplaceDotWithDoubleColon:
    includes: list[CppInclude]
    required_import: PySpecificImport | None = None


type CallMapInfo = (
    CallMapInfoLeftAndRight
    | CallMapInfoCppType
    | CallMapInfoNone
    | CallMapInfoCustomMapping
    | CallMapInfoCustomMappingFromLibrary
    | CallMapInfoCustomMappingStartsWith
    | CallMapInfoCustomMappingStartsWithFromLibrary
    | CallMapInfoReplaceDotWithDoubleColon
)

type NamesMap = dict[str, MapInfo]
type CallsMap = dict[str, CallMapInfo]
type AttrsMap = dict[str, MapInfo]
type FnArgsByValueMap = dict[str, PySpecificImport | None]
type SubscriptableTypesMap = dict[str, PySpecificImport | None]

type NamesCallsOrAttrsMap = NamesMap | CallsMap | AttrsMap
type NamesCallsOrAttrsMapInfo = MapInfo | CallMapInfo
