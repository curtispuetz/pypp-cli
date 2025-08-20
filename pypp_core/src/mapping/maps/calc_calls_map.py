import json
import os
from typing import Callable

from pypp_core.src.config import PyppDirs
from pypp_core.src.handle_expr.h_call.default_map import CALLS_MAP
from pypp_core.src.mapping.maps.util import (
    calc_cpp_includes,
    calc_imp_str,
    calc_required_py_import,
)
from pypp_core.src.mapping.info_types import (
    CallMapInfo,
    CallMapInfoCppType,
    CallMapInfoCustomMappingFromLibrary,
    CallMapInfoCustomMappingStartsWithFromLibrary,
    CallMapInfoLeftAndRight,
    CallMapInfoNone,
    CallMapInfoReplaceDotWithDoubleColon,
    CallsMap,
)

# TODO: similar to above, also have an option that all my_lib includes translate to
#  the coorsponding cpp_include.
# TODO: there will also be an option to ignore certain py imports (as menitoned in a
#  TODO elsewhere). So, remember that in there you could put certain exceptions for
#  py my_lib imports to ignore if you use the 'all' option mentioned above.
# TODO: consider naming caller_str to cpp_caller_str to avoid confusion. And maybe the
#  same for names and attrs if a similar thing exists there.


def _calc_left_and_right_call_map_info(obj: dict) -> CallMapInfoLeftAndRight:
    return CallMapInfoLeftAndRight(obj["left"], obj["right"], calc_cpp_includes(obj))


def _calc_none_call_map_info(obj: dict) -> CallMapInfoNone:
    return CallMapInfoNone(calc_cpp_includes(obj))


def _calc_cpp_call_call_map_info(obj: dict) -> CallMapInfoCppType:
    return CallMapInfoCppType(obj["cpp_call"], calc_cpp_includes(obj))


def _calc_custom_mapping_info(obj: dict) -> CallMapInfoCustomMappingFromLibrary:
    return CallMapInfoCustomMappingFromLibrary(
        "\n".join(obj["mapping_function"]), calc_cpp_includes(obj)
    )


def _calc_custom_mapping_starts_with_info(
    obj: dict,
) -> CallMapInfoCustomMappingStartsWithFromLibrary:
    return CallMapInfoCustomMappingStartsWithFromLibrary(
        "\n".join(obj["mapping_function"]), calc_cpp_includes(obj)
    )


def _calc_replace_dot_with_double_colon_info(
    obj: dict,
) -> CallMapInfoReplaceDotWithDoubleColon:
    return CallMapInfoReplaceDotWithDoubleColon(calc_cpp_includes(obj))


mapping_funcs: dict[str, Callable[[dict], CallMapInfo]] = {
    "left_and_right": _calc_left_and_right_call_map_info,
    "none": _calc_none_call_map_info,
    "cpp_call": _calc_cpp_call_call_map_info,
    "custom_mapping": _calc_custom_mapping_info,
    "custom_mapping_starts_with": _calc_custom_mapping_starts_with_info,
    "replace_dot_with_double_colon": _calc_replace_dot_with_double_colon_info,
}


def calc_calls_map(proj_info: dict, dirs: PyppDirs) -> CallsMap:
    ret = CALLS_MAP.copy()
    for installed_library in proj_info["installed_libraries"]:
        json_path = dirs.calc_bridge_json(installed_library, "calls_map")
        if os.path.isfile(json_path):
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
                                    f"warning: Py++ transpiler already maps the call "
                                    f"'{k}{calc_imp_str(required_import)}'. Library "
                                    f"{installed_library} is overriding this mapping."
                                )
                            ret[k][required_import] = mapping_funcs[mapping_type](v)
                        else:
                            ret[k] = {required_import: mapping_funcs[mapping_type](v)}
                else:
                    raise ValueError(
                        f"invalid type '{mapping_type}' in calls_map.json for "
                        f"'{installed_library}' library. "
                        f"This shouldn't happen because the json should be "
                        f"validated when the library is installed"
                    )
    return ret
