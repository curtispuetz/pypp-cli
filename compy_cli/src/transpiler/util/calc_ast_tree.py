import ast
from pathlib import Path


def calc_ast_tree(file: Path) -> ast.Module:
    assert file.exists(), "Shouldn't happen"
    py_source_code: str = file.read_text()
    ast_tree = ast.parse(py_source_code)
    assert isinstance(ast_tree, ast.Module), "Shouldn't happen"
    return ast_tree
