from dataclasses import dataclass
from pathlib import Path
from pypp_cli.src.transpilers.library.bridge_libs.finder import PyppLibs
from pypp_cli.src.transpilers.library.bridge_libs.models import (
    AngleIncludeModel,
    QuoteIncludeModel,
    RequiredPyImportModel,
)
from pypp_cli.src.transpilers.library.bridge_libs.path_cltr import (
    BridgeJsonPathCltr,
)
from pypp_cli.src.transpilers.library.transpiler.d_types import (
    AngInc,
    CppInclude,
    PyImport,
    PySpecificImpFrom,
    PySpecificImport,
    QInc,
)


def calc_cpp_include(
    quote: QuoteIncludeModel | None, angle: AngleIncludeModel | None
) -> list[CppInclude]:
    ret: list[CppInclude] = []
    if quote is not None:
        for inc_str in quote.root:
            ret.append(QInc(inc_str))
    if angle is not None:
        for inc_str in angle.root:
            ret.append(AngInc(inc_str))
    return ret


def calc_required_py_import(
    d: RequiredPyImportModel | None,
) -> PySpecificImport | None:
    if d is not None:
        if d.module is not None:
            return PySpecificImpFrom(d.module, d.name)
        if d.as_name is not None:
            return PyImport(d.name, d.as_name)
        return PyImport(d.name)
    return None


def calc_imp_str(imp: PySpecificImport | None) -> str:
    return "" if imp is None else f" ({imp})"


@dataclass(frozen=True, slots=True)
class MapCltrAlgo:
    _libs: PyppLibs
    _bridge_json_path_cltr: BridgeJsonPathCltr
    _proj_bridge_json_dir: Path
