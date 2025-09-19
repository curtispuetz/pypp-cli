from typing import Callable
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.y.d_types import (
    PyImp,
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


type CallMapEntry = (
    LeftAndRightEntry
    | ToStringEntry
    | CustomMappingEntry
    | CustomMappingFromLibEntry
    | CustomMappingStartsWithEntry
    | CustomMappingStartsWithFromLibEntry
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
)

type AnnAssignMapEntry = (
    CustomMappingEntry
    | CustomMappingFromLibEntry
    | CustomMappingStartsWithEntry
    | CustomMappingStartsWithFromLibEntry
)


type NameMapValue = dict[PyImp | None, NameMapEntry]
type CallMapValue = dict[PyImp | None, CallMapEntry]
type AttrMapValue = dict[PyImp | None, AttrMapEntry]
type AnnAssignMapValue = dict[PyImp | None, AnnAssignMapEntry]
type FnArgByValueMapValue = set[PyImp | None]
type SubscriptableTypeMapValue = set[PyImp | None]
type NameMap = dict[str, NameMapValue]
type CallMap = dict[str, CallMapValue]
type AttrMap = dict[str, AttrMapValue]
type AnnAssignsMap = dict[str, AnnAssignMapValue]
type FnArgByValueMap = dict[str, FnArgByValueMapValue]
type SubscriptableTypeMap = dict[str, SubscriptableTypeMapValue]


@dataclass(frozen=True, slots=True)
class Maps:
    name: NameMap
    call: CallMap
    attr: AttrMap
    fn_arg_passed_by_value: FnArgByValueMap
    subscriptable_type: SubscriptableTypeMap
    ann_assign: AnnAssignsMap
