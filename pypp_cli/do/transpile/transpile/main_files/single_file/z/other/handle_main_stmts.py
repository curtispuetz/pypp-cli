import ast

from pypp_cli.src.config import SHOULDNT_HAPPEN
from pypp_cli.src.transpilers.library.transpiler.d_types import QInc
from pypp_cli.src.transpilers.library.transpiler.deps import Deps


def handle_main_stmts(stmts: list[ast.stmt], d: Deps) -> str:
    main_stmt = stmts[-1]
    before_main = d.handle_stmts(stmts[:-1])
    # Shouldnt happen because I already check this
    assert isinstance(main_stmt, ast.If), SHOULDNT_HAPPEN
    inside_main = d.handle_stmts(main_stmt.body + [ast.Return(ast.Constant(0))])
    d.add_inc(QInc("pypp_util/main_error_handler.h"))
    return (
        before_main
        + " int main() { try {"
        + inside_main
        + "} catch (...) { pypp::handle_fatal_exception(); return EXIT_FAILURE;} }"
    )
