import ast
from dataclasses import dataclass

from src.util.calc_fn_signature import calc_fn_signature
from src.util.handle_lists import handle_stmts
from src.util.ret_imports import RetImports


@dataclass(frozen=True, slots=True)
class ClassMethod:
    fn_signature: str
    body_str: str


def calc_method(
    node: ast.FunctionDef,
    ret_imports: RetImports,
    handle_stmt,
    handle_expr,
    name_doesnt_start_with_underscore: bool,
) -> ClassMethod:
    assert not (node.name.startswith("__") and node.name.endswith("__")), (
        f"magic method {node.name} for a class is not supported"
    )
    assert node.args.args[0].arg == "self", "first arg must be self"
    fn_signature = calc_fn_signature(
        node,
        ret_imports,
        handle_expr,
        node.name,
        name_doesnt_start_with_underscore,
        skip_first_arg=True,  # because it is self
    )
    body_str: str = handle_stmts(node.body, ret_imports, [], handle_stmt)
    return ClassMethod(fn_signature, body_str)
