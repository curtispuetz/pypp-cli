from dataclasses import dataclass

from pypp_cli.src.transpilers.library.transpiler.d_types import CppInclude

IncMap = dict[str, CppInclude]


@dataclass(frozen=True, slots=True)
class CppIncludes:
    header: set[CppInclude]
    cpp: set[CppInclude]
    include_map: IncMap

    def add_inc(self, inc: CppInclude, in_header: bool):
        if in_header:
            self.header.add(inc)
        else:
            self.cpp.add(inc)

    def contains(self, inc: CppInclude) -> bool:
        return inc in self.header or inc in self.cpp

    def discard(self, inc: CppInclude):
        self.header.discard(inc)
        self.cpp.discard(inc)
