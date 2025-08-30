from dataclasses import dataclass
import json
from pathlib import Path
from typing import Callable
from compy_cli.src.transpiler.maps.d_types import (
    CustomMappingFromLibEntry,
    CustomMappingStartsWithFromLibEntry,
    ReplaceDotWithDoubleColonEntry,
    ToStringEntry,
)
from compy_cli.src.transpiler.maps.util.util import (
    MapCltrAlgo,
    calc_imp_str,
)
from compy_cli.src.transpiler.maps.util.util import (
    calc_cpp_includes,
    calc_required_py_import,
)


def calc_to_string_entry(obj: dict) -> ToStringEntry:
    return ToStringEntry(obj["to"], calc_cpp_includes(obj))


def calc_custom_mapping_from_lib_entry(obj: dict) -> CustomMappingFromLibEntry:
    return CustomMappingFromLibEntry(
        "\n".join(obj["mapping_function"]), calc_cpp_includes(obj)
    )


def calc_custom_mapping_starts_with_from_lib_entry(
    obj: dict,
) -> CustomMappingStartsWithFromLibEntry:
    return CustomMappingStartsWithFromLibEntry(
        "\n".join(obj["mapping_function"]), calc_cpp_includes(obj)
    )


def calc_replace_dot_with_double_colon_entry(
    obj: dict,
) -> ReplaceDotWithDoubleColonEntry:
    return ReplaceDotWithDoubleColonEntry(calc_cpp_includes(obj))


BASE_CALC_ENTRY_FN_MAP: dict[
    str,
    Callable[
        [dict],
        ToStringEntry | CustomMappingFromLibEntry | CustomMappingStartsWithFromLibEntry,
    ],
] = {
    "to_string": calc_to_string_entry,
    "custom_mapping": calc_custom_mapping_from_lib_entry,
    "custom_mapping_starts_with": calc_custom_mapping_starts_with_from_lib_entry,
}


@dataclass(frozen=True, slots=True)
class MapCltr1(MapCltrAlgo):
    def calc_map_1(
        self, base_map, calc_entry_fn_map, json_file_name: str, friendly_name: str
    ):
        ret = base_map.copy()
        for bridge_lib in self._bridge_libs:
            json_path: Path = self._bridge_json_path_cltr.calc_bridge_json(
                bridge_lib, json_file_name
            )
            if json_path.is_file():
                with open(json_path, "r") as f:
                    m: dict = json.load(f)
                # Note: No assertions required here because the structure is
                # (or will be)
                # validated when the library is installed.
                for mapping_type, mapping_vals in m.items():
                    _assert_valid_mapping_type(
                        calc_entry_fn_map,
                        mapping_type,
                        json_file_name,
                        bridge_lib,
                    )
                    for k, v in mapping_vals.items():
                        required_import = calc_required_py_import(v)
                        if k in ret:
                            if required_import in ret[k]:
                                print(
                                    f"warning: Compy transpiler already maps the "
                                    f"{friendly_name} "
                                    f"'{k}{calc_imp_str(required_import)}'. Library "
                                    f"{bridge_lib} is overriding this mapping."
                                )
                            ret[k][required_import] = calc_entry_fn_map[mapping_type](v)
                        else:
                            ret[k] = {
                                required_import: calc_entry_fn_map[mapping_type](v)
                            }
        return ret


def _assert_valid_mapping_type(
    calc_entry_fn_map, mapping_type: str, json_name: str, installed_library: str
):
    assert mapping_type in calc_entry_fn_map, (
        f"invalid key '{mapping_type}' in {json_name}.json for "
        f"'{installed_library}' library. "
        f"This shouldn't happen because the json should be "
        f"validated when the library is installed"
    )
