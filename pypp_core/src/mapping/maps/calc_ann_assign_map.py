import json
from pathlib import Path
from typing import Callable
from pypp_core.src.pypp_dirs import PyppDirs
from pypp_core.src.d_types import PySpecificImpFrom
from pypp_core.src.mapping.info_types import (
    AnnAssignMapInfo,
    AnnAssignMapInfoCustomMappingStartsWith,
    AnnAssignMapInfoCustomMappingStartsWithFromLibrary,
    AnnAssignsMap,
)
from pypp_core.src.mapping.maps.util import (
    calc_cpp_includes,
    calc_imp_str,
    calc_required_py_import,
)
from pypp_core.src.util.inner_strings import calc_inside_rd


def _py_dict(type_cpp: str, value_str: str, target_str: str) -> str:
    return f"{type_cpp} {target_str}({value_str})"


def _uni(type_cpp: str, value_str: str, target_str: str) -> str:
    v: str = calc_inside_rd(value_str)
    if v == "std::monostate":
        v += "{}"
    return f"{type_cpp} {target_str}({v})"


ANN_ASSIGN_MAP: AnnAssignsMap = {
    "PyDict<": {None: AnnAssignMapInfoCustomMappingStartsWith(_py_dict, [])},
    "Uni<": {
        PySpecificImpFrom(
            "pypp_python.union", "Uni"
        ): AnnAssignMapInfoCustomMappingStartsWith(_uni, [])
    },
}


def _calc_custom_mapping_starts_with_info(
    obj: dict,
) -> AnnAssignMapInfoCustomMappingStartsWithFromLibrary:
    return AnnAssignMapInfoCustomMappingStartsWithFromLibrary(
        "\n".join(obj["mapping_function"]), calc_cpp_includes(obj)
    )


mapping_funcs: dict[str, Callable[[dict], AnnAssignMapInfo]] = {
    "custom_mapping_starts_with": _calc_custom_mapping_starts_with_info
}


def calc_ann_assign_map(proj_info: dict, dirs: PyppDirs) -> AnnAssignsMap:
    ret = ANN_ASSIGN_MAP.copy()
    for installed_library in proj_info["installed_libraries"]:
        json_path: Path = dirs.calc_bridge_json(installed_library, "ann_assigns_map")
        if json_path.is_file():
            with open(json_path, "r") as f:
                m: dict = json.load(f)
            # Note: No assertions required here because the structure is (or will be)
            # validated when the library is installed.
            for mapping_type, mapping_vals in m.items():
                if mapping_type in mapping_funcs:
                    for k, v in mapping_vals.items():
                        required_import = calc_required_py_import(v)
                        if k in ret:
                            if required_import in ret[k]:
                                print(
                                    f"warning: Py++ transpiler already maps the ann "
                                    f"assign "
                                    f"'{k}{calc_imp_str(required_import)}'. Library "
                                    f"{installed_library} is overriding this mapping."
                                )
                            ret[k][required_import] = mapping_funcs[mapping_type](v)
                        else:
                            ret[k] = {required_import: mapping_funcs[mapping_type](v)}
                else:
                    raise ValueError(
                        f"invalid type '{mapping_type}' in ann_assigns_map.json for "
                        f"'{installed_library}' library. "
                        f"This shouldn't happen because the json should be "
                        f"validated when the library is installed"
                    )
    return ret
