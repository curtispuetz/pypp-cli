import json
import os
from collections.abc import Callable
from typing import TypeVar

from pypp_core.src.config import PyppDirs
from pypp_core.src.d_types import (
    PySpecificImport,
    AngInc,
    QInc,
    PySpecificImpFrom,
    PyImport,
    CppInclude,
)
from pypp_core.src.mapping.info_types import MapInfo


def calc_cpp_includes(obj: dict) -> list[CppInclude]:
    ret: list[CppInclude] = []
    if "cpp_includes" in obj:
        assert isinstance(obj["cpp_includes"], dict), "cpp_includes must be an object"
        for inc_type, inc_str in obj["cpp_includes"].items():
            if inc_type == "quote_include":
                ret.append(QInc(inc_str))
            elif inc_type == "angle_include":
                ret.append(AngInc(inc_str))
            else:
                raise ValueError(f"invalid type in cpp_includes object: {inc_type}")
    return ret


def calc_required_py_import(obj: dict | None) -> PySpecificImport | None:
    if obj is not None and "required_py_import" in obj:
        req = obj["required_py_import"]
        assert isinstance(req, dict), "required_py_import must be an object"
        assert "name" in req, "required_py_import must specify a name"
        if "module" in req:
            return PySpecificImpFrom(req["module"], req["name"])
        if "as_name" in req:
            return PyImport(req["name"], req["as_name"])
        return PyImport(req["name"])
    return None


def calc_map_info(obj: dict, json_file_name: str) -> MapInfo:
    assert "cpp_type" in obj, (
        f"{json_file_name}.json must specify a cpp_type for each element"
    )
    cpp_includes = calc_cpp_includes(obj)
    return MapInfo(obj["cpp_type"], cpp_includes)


def calc_imp_str(imp: PySpecificImport | None) -> str:
    return "" if imp is None else f" ({imp})"


def calc_common_warning_msg(
    installed_library: str, full_type_str: str, name: str
) -> str:
    return (
        f"Py++ transpiler already maps the {name} '{full_type_str}'. "
        f"Library {installed_library} is overriding this mapping."
    )


T = TypeVar("T")


def load_map(
    default_map: dict[str, dict[PySpecificImport | None, T]],
    proj_info: dict,
    dirs: PyppDirs,
    json_file_name: str,
    value_calc_fn: Callable[[dict, str], T],
    warning_fn: Callable[[str, str], str],
) -> dict[str, dict[PySpecificImport | None, T]]:
    ret = default_map.copy()
    for installed_library in proj_info["installed_libraries"]:
        json_path = dirs.calc_bridge_json(installed_library, json_file_name)
        if os.path.isfile(json_path):
            with open(json_path, "r") as f:
                m: dict = json.load(f)
            for _type, obj in m.items():
                required_import = calc_required_py_import(obj)
                if _type in ret:
                    if required_import in ret[_type]:
                        print(
                            f"warning: {
                                warning_fn(
                                    installed_library,
                                    f'{_type}{calc_imp_str(required_import)}',
                                )
                            }"
                        )
                    ret[_type][required_import] = value_calc_fn(obj, json_file_name)
                else:
                    ret[_type] = {required_import: value_calc_fn(obj, json_file_name)}
    return ret
