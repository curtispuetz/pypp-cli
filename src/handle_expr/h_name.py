import ast

from src.deps import Deps
from src.mapping.types import lookup_cpp_type
from src.util.ret_imports import add_inc


def handle_name(
    node: ast.Name,
    d: Deps,
    skip_cpp_lookup: bool,
    include_in_header: bool,
) -> str:
    if node.id in d.ret_imports.import_map:
        add_inc(d.ret_imports, d.ret_imports.import_map[node.id], include_in_header)
    if skip_cpp_lookup:
        return node.id
    return lookup_cpp_type(node.id, d.ret_imports, include_in_header)
