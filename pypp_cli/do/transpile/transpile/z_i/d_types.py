from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True, slots=True)
class AngInc:
    # Angle Bracket Include
    val: str


@dataclass(frozen=True, slots=True)
class QInc:
    # Quotes Include
    val: str

    @classmethod
    def from_module(cls, module: str) -> "QInc":
        return cls(header_from_module(module))


def header_from_module(module: str) -> str:
    return module.replace(".", "/") + ".h"


CppInclude = Union[AngInc, QInc]


@dataclass(frozen=True, slots=True)
class PySpecificImpFrom:
    frm: str
    name: str


@dataclass(frozen=True, slots=True)
class PyImport:
    name: str
    as_name: str | None = None


type PySpecificImport = Union[PySpecificImpFrom, PyImport]


@dataclass(frozen=True, slots=True)
class ModulePyImports:
    # key: module name, value: list of names imported from that module
    imp_from: dict[str, list[str]]
    imp: set[PyImport]

    def is_imported(self, imp: PySpecificImport) -> bool:
        if isinstance(imp, PyImport):
            return imp in self.imp
        # PySpecificImpFrom
        return imp.frm in self.imp_from and imp.name in self.imp_from[imp.frm]
