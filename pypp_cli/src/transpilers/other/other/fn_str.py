from pypp_cli.src.transpilers.other.transpiler.deps import Deps


import ast
import types


def calc_funcs_in_str(mapping_fn: str) -> list[types.FunctionType]:
    namespace = {"ast": ast, "Deps": Deps}
    exec(mapping_fn, namespace)
    return [obj for obj in namespace.values() if isinstance(obj, types.FunctionType)]
