import ast
import os

from src.config import C_PYTHON_SRC_DIR, C_PYTHON_DIR


def get_main_py_ast_tree(rel_path: str) -> ast.Module:
    file = os.path.join(C_PYTHON_DIR, rel_path)
    assert os.path.exists(file), "Shouldn't happen"
    return _get_tree(file)


def get_src_py_ast_tree(py_src_file: str) -> ast.Module:
    file = os.path.join(C_PYTHON_SRC_DIR, py_src_file)
    assert os.path.exists(file), "Shouldn't happen"
    return _get_tree(file)


def _get_tree(file: str) -> ast.Module:
    with open(file) as py_file:
        py_source_code = py_file.read()
    ast_tree = ast.parse(py_source_code)
    assert isinstance(ast_tree, ast.Module), "Shouldn't happen"
    return ast_tree
