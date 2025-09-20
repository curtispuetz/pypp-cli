import types
from pypp_cli.do.transpile.transpile.y.d_types import AngInc, PyImp, QInc
from pypp_cli.do.transpile.transpile.calc_code.z.deps import Deps
from pypp_cli.do.transpile.transpile.y.maps.d_types import MappingFnStr
import ast


def is_imported(required_imports: set[PyImp | None], d: Deps) -> bool:
    for required_import in required_imports:
        if required_import is None or d.is_imported(required_import):
            return True
    return False


def find_map_entry[T](_map: dict[PyImp | None, T], d: Deps) -> T | None:
    for required_import, map_entry in _map.items():
        if required_import is None or d.is_imported(required_import):
            return map_entry
    return None


def calc_string_fn(info: MappingFnStr) -> types.FunctionType:
    return _calc_mapping_fn(info.mapping_fn_str)


def _calc_mapping_fn(mapping_fn: str) -> types.FunctionType:
    namespace = {
        "ast": ast,
        "Deps": Deps,
        "QInc": QInc,
        "AngInc": AngInc,
        "PyImp": PyImp,
    }
    exec(mapping_fn, namespace)
    # Find the function named "mapping_fn" in the namespace
    for obj in namespace.values():
        if isinstance(obj, types.FunctionType) and obj.__name__ == "mapping_fn":
            return obj
    raise ValueError("No function named 'mapping_fn' found in mapping_functions file.")
