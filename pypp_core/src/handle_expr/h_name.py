import ast

from pypp_core.src.deps import Deps
from pypp_core.src.mapping.names import lookup_cpp_name


def handle_name(node: ast.Name, d: Deps, skip_cpp_lookup: bool) -> str:
    if node.id in d.ret_imports.import_map:
        d.add_inc(d.ret_imports.import_map[node.id])
    if skip_cpp_lookup:
        return node.id
    return lookup_cpp_name(node.id, d)
