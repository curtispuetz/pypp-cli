import ast
import types
from compy_cli.src.transpiler.module.d_types import PySpecificImport
from compy_cli.src.transpiler.module.deps import Deps
from compy_cli.src.transpiler.maps.d_types import MappingFnStr


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


def calc_funcs_in_str(mapping_fn: str) -> list[types.FunctionType]:
    namespace = {"ast": ast, "Deps": Deps}
    exec(mapping_fn, namespace)
    return [obj for obj in namespace.values() if isinstance(obj, types.FunctionType)]
