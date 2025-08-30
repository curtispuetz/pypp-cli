from dataclasses import dataclass
from compy_cli.src.transpiler.bridge_json_path_cltr import BridgeJsonPathCltr
from compy_cli.src.transpiler.module.d_types import (
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
    if "cpp_includes" in obj:
        for inc_type, inc_str in obj["cpp_includes"].items():
            if inc_type == "quote_include":
                ret.append(QInc(inc_str))
            elif inc_type == "angle_include":
                ret.append(AngInc(inc_str))
            else:
                raise ValueError(
                    f"invalid type in cpp_includes object: {inc_type}. {_ERROR_STR}"
                )
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
