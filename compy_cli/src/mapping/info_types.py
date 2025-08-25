from collections.abc import Callable
from dataclasses import dataclass

from compy_cli.src.d_types import PySpecificImport, CppInclude


@dataclass(frozen=True, slots=True)
class ToStringEntry:
    to: str
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class LeftAndRightEntry:
    left: str
    right: str
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class CustomMappingEntry:
    mapping_fn: Callable
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class MappingFnStr:
    mapping_fn_str: str


@dataclass(frozen=True, slots=True)
class CustomMappingFromLibEntry(MappingFnStr):
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class CustomMappingStartsWithEntry:
    mapping_fn: Callable
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class CustomMappingStartsWithFromLibEntry(MappingFnStr):
    includes: list[CppInclude]


@dataclass(frozen=True, slots=True)
class ReplaceDotWithDoubleColonEntry:
    includes: list[CppInclude]


type CallMapInfo = (
    LeftAndRightEntry
    | ToStringEntry
    | CustomMappingEntry
    | CustomMappingFromLibEntry
    | CustomMappingStartsWithEntry
    | CustomMappingStartsWithFromLibEntry
    | ReplaceDotWithDoubleColonEntry
)

type AnnAssignMapInfo = (
    CustomMappingStartsWithEntry | CustomMappingStartsWithFromLibEntry
)


type NameMapValue = dict[PySpecificImport | None, ToStringEntry]
type CallMapValue = dict[PySpecificImport | None, CallMapInfo]
type AttrMapValue = dict[PySpecificImport | None, ToStringEntry]
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
