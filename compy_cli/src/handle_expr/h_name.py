import ast

from compy_cli.src.deps import Deps
from compy_cli.src.mapping.names import lookup_cpp_name


def handle_name(node: ast.Name, d: Deps) -> str:
    if node.id in d.ret_imports.include_map:
        d.add_inc(d.ret_imports.include_map[node.id])
    return lookup_cpp_name(node.id, d)
