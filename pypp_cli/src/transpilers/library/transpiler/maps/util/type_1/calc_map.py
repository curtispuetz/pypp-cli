from dataclasses import dataclass
from typing import Callable
from pypp_cli.src.transpilers.library.transpiler.d_types import PySpecificImport
from pypp_cli.src.transpilers.library.transpiler.maps.d_types import (
    CustomMappingFromLibEntry,
    CustomMappingStartsWithFromLibEntry,
    ReplaceDotWithDoubleColonEntry,
    ToStringEntry,
)
from pypp_cli.src.transpilers.library.transpiler.maps.util.type_1.helper import (
    MapCltr1Helper,
)
from pypp_cli.src.transpilers.library.transpiler.maps.util.util import (
    MapCltrAlgo,
)
from pypp_cli.src.transpilers.library.transpiler.maps.util.util import (
    calc_cpp_includes,
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
    return ReplaceDotWithDoubleColonEntry(calc_cpp_includes(obj), False)


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
class MapCltr1[T](MapCltrAlgo):
    type Map = dict[str, dict[PySpecificImport | None, T]]

    def calc_map_1(
        self,
        base_map: Map,
        calc_entry_fn_map: dict[str, Callable[[dict], T]],
        json_file_name: str,
        friendly_name: str,
    ):
        helper = MapCltr1Helper(
            self._libs,
            self._bridge_json_path_cltr,
            self._proj_bridge_json_dir,
            base_map,
            calc_entry_fn_map,
            json_file_name,
            friendly_name,
        )
        return helper.calc()
