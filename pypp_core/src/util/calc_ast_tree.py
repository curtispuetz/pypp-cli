import ast
import os


def calc_ast_tree(file: str) -> ast.Module:
    assert os.path.exists(file), "Shouldn't happen"
    with open(file) as py_file:
        py_source_code = py_file.read()
    ast_tree = ast.parse(py_source_code)
    assert isinstance(ast_tree, ast.Module), "Shouldn't happen"
    return ast_tree
