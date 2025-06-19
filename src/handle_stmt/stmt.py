import ast

from src.handle_expr.expr import handle_expr
from src.handle_stmt.h_ann_assign import handle_ann_assign
from src.handle_stmt.h_assign import handle_assign
from src.handle_stmt.h_aug_assign import handle_aug_assign
from src.handle_stmt.h_expr import handle_stmt_expr
from src.handle_stmt.h_fn_def import handle_fn_def
from src.handle_stmt.h_for import handle_for
from src.handle_stmt.h_if import handle_if
from src.handle_stmt.h_raise import handle_raise
from src.handle_stmt.h_return import handle_return
from src.handle_stmt.h_try import handle_try
from src.handle_stmt.h_while import handle_while
from src.handle_stmt.h_width import handle_with
from src.util.ret_imports import RetImports


def handle_stmt(node: ast.stmt, ret_imports: RetImports, ret_h_file: list[str]) -> str:
    if isinstance(node, ast.FunctionDef):
        return handle_fn_def(node, ret_imports, ret_h_file, handle_stmt, handle_expr)
    if isinstance(node, ast.If):
        return handle_if(node, ret_imports, ret_h_file, handle_stmt, handle_expr)
    if isinstance(node, ast.AnnAssign):
        return handle_ann_assign(node, ret_imports, handle_expr)
    if isinstance(node, ast.Return):
        return handle_return(node, ret_imports, handle_expr)
    if isinstance(node, ast.Assign):
        return handle_assign(node, ret_imports, handle_expr)
    if isinstance(node, ast.Expr):
        return handle_stmt_expr(node, ret_imports, handle_expr)
    if isinstance(node, ast.AugAssign):
        return handle_aug_assign(node, ret_imports, handle_expr)
    if isinstance(node, ast.For):
        return handle_for(node, ret_imports, ret_h_file, handle_stmt, handle_expr)
    if isinstance(node, ast.While):
        return handle_while(node, ret_imports, ret_h_file, handle_stmt, handle_expr)
    if isinstance(node, ast.Break):
        return "break;"
    if isinstance(node, ast.Continue):
        return "continue;"
    if isinstance(node, ast.Raise):
        return handle_raise(node, ret_imports, handle_expr)
    if isinstance(node, ast.Try):
        return handle_try(node, ret_imports, ret_h_file, handle_stmt)
    if isinstance(node, ast.With):
        return handle_with(node, ret_imports, ret_h_file, handle_stmt, handle_expr)
    if isinstance(node, ast.ImportFrom) or isinstance(node, ast.Import):
        raise Exception("import statements after other code is not supported")
    raise Exception(f"code stmt type {node} not handled")
