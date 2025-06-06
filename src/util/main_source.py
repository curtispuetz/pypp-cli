import ast
from pathlib import Path

from src.d_types import CppInclude
from src.handle_stmt.stmt import handle_stmts
from src.include_str import calc_includes_string
from src.util.handle_main_stmts import handle_main_stmts


def calc_main_cpp_source(main_py: ast.Module) -> str:
    ret_imports = set()
    cpp_source_minus_includes: str = handle_main_stmts(main_py.body, ret_imports)
    cpp_includes: str = calc_includes_string(ret_imports)
    return cpp_includes + cpp_source_minus_includes


def calc_src_file_cpp_and_h_source(src_py: ast.Module, h_file: Path) -> tuple[str, str]:
    ret_imports: set[CppInclude] = set()
    ret_h_file: list[str] = []
    cpp_source_minus_include: str = handle_stmts(src_py.body, ret_imports, ret_h_file)
    cpp_include = f'#include "{h_file}"\n\n'
    ret_cpp_str = cpp_include + cpp_source_minus_include

    h_includes: str = calc_includes_string(ret_imports)
    ret_h_str: str = "#pragma once\n\n" + h_includes + " ".join(ret_h_file)

    return ret_cpp_str, ret_h_str
