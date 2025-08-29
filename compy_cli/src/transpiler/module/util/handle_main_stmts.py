import ast

from compy_cli.src.transpiler.module.d_types import QInc
from compy_cli.src.transpiler.module.deps import Deps


def handle_main_stmts(stmts: list[ast.stmt], d: Deps) -> str:
    main_stmt = stmts[-1]
    if not _is_proper_main(main_stmt):
        raise Exception(
            "A correctly defined main guard as the last stmt in a root python file is "
            "required"
        )
    before_main = d.handle_stmts(stmts[:-1])
    assert isinstance(main_stmt, ast.If), "shouldn't happen"
    inside_main = d.handle_stmts(main_stmt.body + [ast.Return(ast.Constant(0))])
    d.add_inc(QInc("compy_util/main_error_handler.h"))
    return (
        before_main
        + " int main() { try {"
        + inside_main
        + "} catch (...) { handle_fatal_exception(); return EXIT_FAILURE;} }"
    )


def _is_proper_main(node: ast.stmt) -> bool:
    if not isinstance(node, ast.If):
        return False
    if len(node.orelse) != 0:
        return False
    if not isinstance(node.test, ast.Compare):
        return False
    if not isinstance(node.test.left, ast.Name):
        return False
    if node.test.left.id != "__name__":
        return False
    if len(node.test.ops) != 1:
        return False
    if not isinstance(node.test.ops[0], ast.Eq):
        return False
    if len(node.test.comparators) != 1:
        return False
    comp = node.test.comparators[0]
    if not isinstance(comp, ast.Constant):
        return False
    if comp.value != "__main__":
        return False
    return True
