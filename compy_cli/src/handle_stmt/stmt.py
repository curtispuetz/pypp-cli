import ast

from compy_cli.src.deps import Deps
from compy_cli.src.handle_stmt.h_ann_assign import handle_ann_assign
from compy_cli.src.handle_stmt.h_assert import handle_assert
from compy_cli.src.handle_stmt.h_assign import handle_assign
from compy_cli.src.handle_stmt.h_aug_assign import handle_aug_assign
from compy_cli.src.handle_stmt.h_class_def.h_class_def import handle_class_def
from compy_cli.src.handle_stmt.h_expr import handle_stmt_expr
from compy_cli.src.handle_stmt.h_fn_def import handle_fn_def
from compy_cli.src.handle_stmt.h_for import handle_for
from compy_cli.src.handle_stmt.h_if import handle_if
from compy_cli.src.handle_stmt.h_raise import handle_raise
from compy_cli.src.handle_stmt.h_return import handle_return
from compy_cli.src.handle_stmt.h_try import handle_try
from compy_cli.src.handle_stmt.h_type_alias import handle_type_alias
from compy_cli.src.handle_stmt.h_while import handle_while
from compy_cli.src.handle_stmt.h_with import handle_with


def handle_stmt(node: ast.stmt, d: Deps) -> str:
    if isinstance(node, ast.FunctionDef):
        return handle_fn_def(node, d)
    if isinstance(node, ast.ClassDef):
        return handle_class_def(node, d)
    if isinstance(node, ast.If):
        return handle_if(node, d)
    if isinstance(node, ast.AnnAssign):
        return handle_ann_assign(node, d)
    if isinstance(node, ast.Return):
        return handle_return(node, d)
    if isinstance(node, ast.Assign):
        return handle_assign(node, d)
    if isinstance(node, ast.Expr):
        return handle_stmt_expr(node, d)
    if isinstance(node, ast.AugAssign):
        return handle_aug_assign(node, d)
    if isinstance(node, ast.For):
        return handle_for(node, d)
    if isinstance(node, ast.While):
        return handle_while(node, d)
    if isinstance(node, ast.Break):
        return "break;"
    if isinstance(node, ast.Continue):
        return "continue;"
    if isinstance(node, ast.Raise):
        return handle_raise(node, d)
    if isinstance(node, ast.Try):
        return handle_try(node, d)
    if isinstance(node, ast.With):
        return handle_with(node, d)
    if isinstance(node, ast.Assert):
        return handle_assert(node, d)
    if isinstance(node, ast.TypeAlias):
        return handle_type_alias(node, d)
    if isinstance(node, (ast.ImportFrom, ast.Import)):
        raise Exception(
            "import statements are only supported at the top of the file before any "
            "other code."
        )
    if isinstance(node, ast.Pass):
        raise Exception("pass keyword is not generally supported")
    raise Exception(f"code stmt type {node} not handled")
