import ast
import os
from pathlib import Path

from src.config import C_PYTHON_MAIN_FILE, C_PYTHON_SRC_DIR


def get_main_py_ast_tree() -> ast.Module:
    assert os.path.exists(C_PYTHON_MAIN_FILE), "main.py must be defined; file not found"
    return _get_tree(C_PYTHON_MAIN_FILE)


def get_src_py_ast_tree(py_src_file: Path) -> ast.Module:
    file = os.path.join(C_PYTHON_SRC_DIR, py_src_file)
    assert os.path.exists(file), "Shouldn't happen"
    return _get_tree(file)


def _get_tree(file: str) -> ast.Module:
    with open(file) as py_file:
        py_source_code = py_file.read()
    ast_tree = ast.parse(py_source_code)
    assert isinstance(ast_tree, ast.Module), "Shouldn't happen"
    return ast_tree
