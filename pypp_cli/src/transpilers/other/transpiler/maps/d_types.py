from typing import Callable
from dataclasses import dataclass

from pypp_cli.src.transpilers.other.transpiler.d_types import (
    PySpecificImport,
    CppInclude,
)


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
    add_pypp_namespace: bool


type CallMapEntry = (
    LeftAndRightEntry
    | ToStringEntry
    | CustomMappingEntry
    | CustomMappingFromLibEntry
    | CustomMappingStartsWithEntry
    | CustomMappingStartsWithFromLibEntry
    | ReplaceDotWithDoubleColonEntry
)

type NameMapEntry = (
    ToStringEntry
    | CustomMappingEntry
    | CustomMappingFromLibEntry
    | CustomMappingStartsWithEntry
    | CustomMappingStartsWithFromLibEntry
)

type AttrMapEntry = (
    ToStringEntry
    | CustomMappingEntry
    | CustomMappingFromLibEntry
    | CustomMappingStartsWithEntry
    | CustomMappingStartsWithFromLibEntry
    | ReplaceDotWithDoubleColonEntry
)

type AnnAssignMapEntry = (
    CustomMappingEntry
    | CustomMappingFromLibEntry
    | CustomMappingStartsWithEntry
    | CustomMappingStartsWithFromLibEntry
)


type NameMapValue = dict[PySpecificImport | None, NameMapEntry]
type CallMapValue = dict[PySpecificImport | None, CallMapEntry]
type AttrMapValue = dict[PySpecificImport | None, AttrMapEntry]
type AnnAssignMapValue = dict[PySpecificImport | None, AnnAssignMapEntry]
type FnArgByValueMapValue = set[PySpecificImport | None]
type SubscriptableTypeMapValue = set[PySpecificImport | None]
type NameMap = dict[str, NameMapValue]
type CallMap = dict[str, CallMapValue]
type AttrMap = dict[str, AttrMapValue]
type AnnAssignsMap = dict[str, AnnAssignMapValue]
type FnArgByValueMap = dict[str, FnArgByValueMapValue]
type SubscriptableTypeMap = dict[str, SubscriptableTypeMapValue]
