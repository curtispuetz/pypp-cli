import types
from compy_cli.src.transpilers.other.module.d_types import PySpecificImport
from compy_cli.src.transpilers.other.transpiler.deps import Deps
from compy_cli.src.transpilers.other.maps.d_types import MappingFnStr
from compy_cli.src.transpilers.other.other.fn_str import calc_funcs_in_str


def is_one(r: set[PySpecificImport | None], d: Deps) -> bool:
    if None in r:
        return True
    for required_import in r:
        if required_import is not None and d.is_imported(required_import):
            return True
    return False


def find_map_entry[T](v: dict[PySpecificImport | None, T], d: Deps) -> T | None:
    for required_import, map_info in v.items():
        if required_import is not None and d.is_imported(required_import):
            return map_info
    if None in v:
        return v[None]
    return None


def calc_string_fn(info: MappingFnStr) -> types.FunctionType:
    return calc_funcs_in_str(info.mapping_fn_str)[0]
