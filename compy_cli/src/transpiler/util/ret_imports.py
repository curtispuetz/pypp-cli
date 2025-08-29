from dataclasses import dataclass

from compy_cli.src.transpiler.d_types import CppInclude

IncMap = dict[str, CppInclude]


@dataclass(frozen=True, slots=True)
class RetImports:
    header: set[CppInclude]
    cpp: set[CppInclude]
    include_map: IncMap


def add_inc(ret_imports: RetImports, inc: CppInclude, in_header: bool):
    if in_header:
        ret_imports.header.add(inc)
    else:
        ret_imports.cpp.add(inc)
