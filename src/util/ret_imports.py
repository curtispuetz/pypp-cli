from dataclasses import dataclass

from src.d_types import CppInclude

ImpMap = dict[str, CppInclude]


@dataclass(frozen=True, slots=True)
class RetImports:
    header: set[CppInclude]
    cpp: set[CppInclude]
    import_map: ImpMap


def add_inc(ret_imports: RetImports, inc: CppInclude, in_header: bool = False):
    if in_header:
        ret_imports.header.add(inc)
    else:
        ret_imports.cpp.add(inc)
