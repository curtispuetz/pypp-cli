import ast

from src.d_types import CppInclude
from src.mapping.types import lookup_cpp_type


def handle_name(
    node: ast.Name, ret_imports: set[CppInclude], skip_cpp_lookup: bool
) -> str:
    if skip_cpp_lookup:
        return node.id
    return lookup_cpp_type(node.id, ret_imports)
