from dataclasses import dataclass
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


_ERROR_STR = (
    "This shouldn't happen because the json schema should have been validated "
    "on library install"
)


def calc_cpp_includes(obj: dict) -> list[CppInclude]:
    ret: list[CppInclude] = []
    if "quote_includes" in obj:
        for inc_str in obj["quote_includes"]:
            ret.append(QInc(inc_str))
    if "angle_includes" in obj:
        for inc_str in obj["angle_includes"]:
            ret.append(AngInc(inc_str))
    return ret


def calc_required_py_import(obj: dict | None) -> PySpecificImport | None:
    if obj is not None and "required_py_import" in obj:
        req = obj["required_py_import"]
        if "module" in req:
            return PySpecificImpFrom(req["module"], req["name"])
        if "as_name" in req:
            return PyImport(req["name"], req["as_name"])
        return PyImport(req["name"])
    return None


def calc_imp_str(imp: PySpecificImport | None) -> str:
    return "" if imp is None else f" ({imp})"


@dataclass(frozen=True, slots=True)
class MapCltrAlgo:
    _bridge_libs: list[str]
    _bridge_json_path_cltr: BridgeJsonPathCltr
