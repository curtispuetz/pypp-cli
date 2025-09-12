import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps


def handle_while(node: ast.While, d: Deps) -> str:
    if len(node.orelse) != 0:
        d.value_err_no_ast("While loop else not supported")
    body_str = d.handle_stmts(node.body)
    test_str = d.handle_expr(node.test)
    return f"while ({test_str})" + "{" + body_str + "}"
