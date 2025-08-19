import json
import os

from pypp_core.src.config import PyppDirs
from pypp_core.src.handle_expr.h_call.default_map import CALLS_MAP
from pypp_core.src.mapping.maps.util import (
    calc_cpp_includes,
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
)

# TODO: rename 'cpp_type' in the calls_map.json to 'cpp_call'
# TODO: a system for the bridge jsons where you can specify certain py imports that
#  should be translated directly to the coorsponding cpp include (i.e. my_lib.a should
#  go to quote includes my_lib/a.h). This will make it so that you do not have to
#  specify cpp_includes and required_py_import everywhere in a bunch of jsons.
# TODO: similar to above, also have an option that all my_lib includes translate to
#  the coorsponding cpp_include.
# TODO: there will also be an option to ignore certain py imports (as menitoned in a
#  TODO elsewhere). So, remember that in there you could put certain exceptions for
#  py my_lib imports to ignore if you use the 'all' option mentioned above.
# TODO: consider naming caller_str to cpp_caller_str to avoid confusion. And maybe the
#  same for names and attrs if a similar thing exists there.

# TODO: the Py required import should be part of the key! Then you can have two things
#  with the same names but from different places. This might be true for other maps as
#  well.


def _calc_left_and_right_call_map_info(obj: dict) -> CallMapInfoLeftAndRight:
    return CallMapInfoLeftAndRight(
        obj["left"], obj["right"], calc_cpp_includes(obj), calc_required_py_import(obj)
    )


def _calc_none_call_map_info(obj: dict) -> CallMapInfoNone:
    return CallMapInfoNone(calc_cpp_includes(obj), calc_required_py_import(obj))


def _calc_cpp_type_call_map_info(obj: dict) -> CallMapInfoCppType:
    return CallMapInfoCppType(
        obj["cpp_type"], calc_cpp_includes(obj), calc_required_py_import(obj)
    )


def _calc_custom_mapping_info(obj: dict) -> CallMapInfoCustomMappingFromLibrary:
    return CallMapInfoCustomMappingFromLibrary(
        "\n".join(obj["mapping_function"]),
        calc_cpp_includes(obj),
        calc_required_py_import(obj),
    )


def _calc_custom_mapping_starts_with_info(
    obj: dict,
) -> CallMapInfoCustomMappingStartsWithFromLibrary:
    return CallMapInfoCustomMappingStartsWithFromLibrary(
        "\n".join(obj["mapping_function"]),
        calc_cpp_includes(obj),
        calc_required_py_import(obj),
    )


def _calc_replace_dot_with_double_colon_info(
    obj: dict,
) -> CallMapInfoReplaceDotWithDoubleColon:
    return CallMapInfoReplaceDotWithDoubleColon(
        calc_cpp_includes(obj),
        calc_required_py_import(obj),
    )


def calc_calls_map(proj_info: dict, dirs: PyppDirs) -> dict[str, CallMapInfo]:
    ret = CALLS_MAP.copy()
    for installed_library in proj_info["installed_libraries"]:
        json_path = dirs.calc_bridge_json(installed_library, "calls_map")
        if os.path.isfile(json_path):
            with open(json_path, "r") as f:
                m: dict = json.load(f)
            # Note: No assertions required here because the structure is (or will be)
            # validated when the library is installed.
            for mapping_type, mapping_vals in m.items():
                if mapping_type == "left_and_right":
                    for k, v in mapping_vals.items():
                        ret[k] = _calc_left_and_right_call_map_info(v)
                elif mapping_type == "none":
                    for k, v in mapping_vals.items():
                        ret[k] = _calc_none_call_map_info(v)
                elif mapping_type == "cpp_type":
                    for k, v in mapping_vals.items():
                        ret[k] = _calc_cpp_type_call_map_info(v)
                elif mapping_type == "custom_mapping":
                    for k, v in mapping_vals.items():
                        ret[k] = _calc_custom_mapping_info(v)
                elif mapping_type == "custom_mapping_starts_with":
                    for k, v in mapping_vals.items():
                        ret[k] = _calc_custom_mapping_starts_with_info(v)
                elif mapping_type == "replace_dot_with_double_colon":
                    for k, v in mapping_vals.items():
                        ret[k] = _calc_replace_dot_with_double_colon_info(v)
                else:
                    raise ValueError(
                        f"invalid type '{mapping_type}' in calls_map.json for "
                        f"'{installed_library}' library. "
                        f"This shouldn't happen because the json should be "
                        f"validated when the library is installed"
                    )
    return ret
