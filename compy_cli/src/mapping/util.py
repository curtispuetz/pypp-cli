import ast
import types
from compy_cli.src.d_types import PySpecificImport
from compy_cli.src.deps import Deps
from compy_cli.src.mapping.d_types import MappingFnStr


def is_one(r: set[PySpecificImport | None], d: Deps) -> bool:
    if None in r:
        return True
    for required_import in r:
        if required_import is not None and d.is_imported(required_import):
            return True
    return False


def find_map_entry[T](r: dict[PySpecificImport | None, T], d: Deps) -> T | None:
    for required_import, map_info in r.items():
        if required_import is not None and d.is_imported(required_import):
            return map_info
    if None in r:
        return r[None]
    return None


def calc_string_fn(
    info: MappingFnStr,
    json_file_name: str,
) -> types.FunctionType:
    namespace = {"ast": ast, "Deps": Deps}
    exec(info.mapping_fn_str, namespace)
    funcs = [obj for obj in namespace.values() if isinstance(obj, types.FunctionType)]
    # TODO: validate mapping function on install and remove this assertion.
    assert len(funcs) == 1, (
        "Expected exactly one function in mapping_function string from "
        f"{json_file_name}.json in an installed bridge-library. "
        "You shouldn't be seeing this error "
        "because the mapping_function should have been "
        "validated when the library was "
        "installed."
    )
    return funcs[0]
