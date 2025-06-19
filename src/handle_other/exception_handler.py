import ast

from src.d_types import AngInc
from src.mapping.exceptions import lookup_cpp_exception_type
from src.util.handle_lists import handle_stmts
from src.util.ret_imports import RetImports, add_inc


def handle_exception_handlers(
    nodes: list[ast.ExceptHandler],
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_stmt,
) -> str:
    return " ".join(
        _handle_exception_handler(node, ret_imports, ret_h_file, handle_stmt)
        for node in nodes
    )


def _handle_exception_handler(
    node: ast.ExceptHandler,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_stmt,
) -> str:
    body_str = handle_stmts(node.body, ret_imports, ret_h_file, handle_stmt)
    exe_str: str
    if node.type is not None:
        assert isinstance(node.type, ast.Name), "Shouldn't happen"
        assert isinstance(node.type.id, str), "Shouldn't happen"
        exe_str = f"const {lookup_cpp_exception_type(node.type.id, ret_imports)}&"
        if node.name is not None:
            assert isinstance(node.name, str), "Shouldn't happen"
            exe_str += f" pypp_{node.name}"
            add_inc(ret_imports, AngInc("string"))
            body_str = f"std::string {node.name} = pypp_{node.name}.what(); " + body_str
    else:
        exe_str = "..."
    return f"catch ({exe_str})" + "{" + body_str + "}"
