import ast

from src.mapping.types import lookup_cpp_type
from src.util.ret_imports import RetImports, add_inc


def handle_name(
    node: ast.Name,
    ret_imports: RetImports,
    skip_cpp_lookup: bool,
    include_in_header: bool,
) -> str:
    if node.id in ret_imports.import_map:
        add_inc(ret_imports, ret_imports.import_map[node.id], include_in_header)
    if skip_cpp_lookup:
        return node.id
    return lookup_cpp_type(node.id, ret_imports, include_in_header)
