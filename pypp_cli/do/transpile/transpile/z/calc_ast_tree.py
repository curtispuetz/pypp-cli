import ast
from pathlib import Path

from pypp_cli.do.transpile.transpile.transpile.z.config import SHOULDNT_HAPPEN


def calc_ast(file: Path) -> ast.Module:
    assert file.exists(), SHOULDNT_HAPPEN
    py_code: str = file.read_text()
    ast_tree = ast.parse(py_code)
    assert isinstance(ast_tree, ast.Module), (
        f"Py++ only supports modules. {file} appears not to be a module."
    )
    return ast_tree
