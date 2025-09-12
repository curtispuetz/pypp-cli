import types
from pypp_cli.src.transpilers.other.transpiler.d_types import PySpecificImport
from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.maps.d_types import MappingFnStr
from pypp_cli.src.transpilers.other.other.fn_str import calc_funcs_in_str


def is_imported(required_imports: set[PySpecificImport | None], d: Deps) -> bool:
    for required_import in required_imports:
        if required_import is None or d.is_imported(required_import):
            return True
    return False


def find_map_entry[T](map: dict[PySpecificImport | None, T], d: Deps) -> T | None:
    for required_import, map_entry in map.items():
        if required_import is None or d.is_imported(required_import):
            return map_entry
    return None


def calc_string_fn(info: MappingFnStr) -> types.FunctionType:
    return calc_funcs_in_str(info.mapping_fn_str)[0]
