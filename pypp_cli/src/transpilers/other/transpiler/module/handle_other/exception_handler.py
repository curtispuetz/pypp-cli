import ast

from pypp_cli.src.transpilers.other.transpiler.d_types import AngInc
from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.mapping.exceptions import (
    lookup_cpp_exception_type,
)


def handle_exception_handlers(nodes: list[ast.ExceptHandler], d: Deps) -> str:
    return " ".join(_handle_exception_handler(node, d) for node in nodes)


def _handle_exception_handler(node: ast.ExceptHandler, d: Deps) -> str:
    body_str = d.handle_stmts(node.body)
    exc_str: str
    if node.type is not None:
        if not isinstance(node.type, ast.Name):
            d.value_err("Can only catch one exception type at a time", node.type)
        name_str = d.handle_expr(node.type)
        exc_str = f"const {lookup_cpp_exception_type(name_str, d)}&"
        if node.name is not None:
            assert isinstance(node.name, str), "Shouldn't happen"
            exc_str += f" pypp_pseudo_name_{node.name}"
            d.add_inc(AngInc("string"))
            body_str = (
                f"std::string {node.name} = pypp_pseudo_name_{node.name}.msg_; "
                + body_str
            )
    else:
        exc_str = "..."
    return f"catch ({exc_str})" + "{" + body_str + "}"
