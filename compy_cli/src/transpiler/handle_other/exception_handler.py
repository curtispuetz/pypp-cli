import ast

from compy_cli.src.transpiler.d_types import AngInc
from compy_cli.src.transpiler.deps import Deps
from compy_cli.src.transpiler.mapping.exceptions import lookup_cpp_exception_type


def handle_exception_handlers(nodes: list[ast.ExceptHandler], d: Deps) -> str:
    return " ".join(_handle_exception_handler(node, d) for node in nodes)


def _handle_exception_handler(node: ast.ExceptHandler, d: Deps) -> str:
    body_str = d.handle_stmts(node.body)
    exc_str: str
    if node.type is not None:
        assert isinstance(node.type, ast.Name), "Shouldn't happen"
        assert isinstance(node.type.id, str), "Shouldn't happen"
        exc_str = f"const {lookup_cpp_exception_type(node.type.id, d)}&"
        if node.name is not None:
            assert isinstance(node.name, str), "Shouldn't happen"
            exc_str += f" compy_{node.name}"
            d.add_inc(AngInc("string"))
            body_str = (
                f"std::string {node.name} = compy_{node.name}.what(); " + body_str
            )
    else:
        exc_str = "..."
    return f"catch ({exc_str})" + "{" + body_str + "}"
