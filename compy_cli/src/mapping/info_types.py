from collections.abc import Callable
from dataclasses import dataclass

from compy_cli.src.d_types import PySpecificImport, CppInclude


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
class MappingFnStr:
    mapping_fn_str: str


@dataclass(frozen=True, slots=True)
class CallMapInfoCustomMappingFromLibrary(MappingFnStr):
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class CallMapInfoCustomMappingStartsWith:
    mapping_fn: Callable
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class CallMapInfoCustomMappingStartsWithFromLibrary(MappingFnStr):
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


@dataclass(frozen=True, slots=True)
class AnnAssignMapInfoCustomMappingStartsWith:
    mapping_fn: Callable
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class AnnAssignMapInfoCustomMappingStartsWithFromLibrary(MappingFnStr):
    includes: list[CppInclude]


type AnnAssignMapInfo = (
    AnnAssignMapInfoCustomMappingStartsWith
    | AnnAssignMapInfoCustomMappingStartsWithFromLibrary
)


type NameMapValue = dict[PySpecificImport | None, MapInfo]
type CallMapValue = dict[PySpecificImport | None, CallMapInfo]
type AttrMapValue = dict[PySpecificImport | None, MapInfo]
type AnnAssignMapValue = dict[PySpecificImport | None, AnnAssignMapInfo]
type FnArgByValueMapValue = dict[PySpecificImport | None, None]
type SubscriptableTypeMapValue = dict[PySpecificImport | None, None]
type NameMap = dict[str, NameMapValue]
type CallMap = dict[str, CallMapValue]
type AttrMap = dict[str, AttrMapValue]
type FnArgByValueMap = dict[str, FnArgByValueMapValue]
type SubscriptableTypeMap = dict[str, SubscriptableTypeMapValue]
type AnnAssignsMap = dict[str, AnnAssignMapValue]

type NameOrAttrMap = NameMap | AttrMap
type NameCallOrAttrMapValue = NameMapValue | AttrMapValue | CallMapValue
