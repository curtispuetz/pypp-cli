import types
from pypp_cli.do.transpile.transpile.z_i.d_types import PySpecificImport
from pypp_cli.do.transpile.transpile.handle.z.deps import Deps
from pypp_cli.do.transpile.transpile.z_i.maps.d_types import MappingFnStr
import ast


def is_imported(required_imports: set[PySpecificImport | None], d: Deps) -> bool:
    for required_import in required_imports:
        if required_import is None or d.is_imported(required_import):
            return True
    return False


def find_map_entry[T](_map: dict[PySpecificImport | None, T], d: Deps) -> T | None:
    for required_import, map_entry in _map.items():
        if required_import is None or d.is_imported(required_import):
            return map_entry
    return None


def calc_string_fn(info: MappingFnStr) -> types.FunctionType:
    return _calc_funcs_in_str(info.mapping_fn_str)[0]


def _calc_funcs_in_str(mapping_fn: str) -> list[types.FunctionType]:
    namespace = {"ast": ast, "Deps": Deps}
    exec(mapping_fn, namespace)
    return [obj for obj in namespace.values() if isinstance(obj, types.FunctionType)]
