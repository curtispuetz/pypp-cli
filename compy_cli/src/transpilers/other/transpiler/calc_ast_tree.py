import ast
from pathlib import Path


def calc_ast(file: Path) -> ast.Module:
    assert file.exists(), "Shouldn't happen"
    py_code: str = file.read_text()
    ast_tree = ast.parse(py_code)
    assert isinstance(ast_tree, ast.Module), (
        f"Compy only supports modules. {file} appears not to be a module."
    )
    return ast_tree
