import ast

from src.handle_stmt.stmt import handle_stmt
from src.util.calc_includes import calc_includes_for_main_file, calc_includes
from src.util.handle_lists import handle_stmts, handle_import_stmts
from src.util.handle_main_stmts import handle_main_stmts
from src.util.ret_imports import RetImports


def calc_main_cpp_source(main_py: ast.Module) -> str:
    imp_map, i = handle_import_stmts(main_py.body)
    ret_imports = RetImports(set(), set(), imp_map)
    cpp_source_minus_includes: str = handle_main_stmts(main_py.body[i:], ret_imports)
    cpp_includes: str = calc_includes_for_main_file(ret_imports)
    return cpp_includes + cpp_source_minus_includes


def calc_src_file_cpp_and_h_source(src_py: ast.Module, h_file: str) -> tuple[str, str]:
    imp_map, i = handle_import_stmts(src_py.body)
    ret_imports = RetImports(set(), set(), imp_map)
    ret_h_file: list[str] = []
    cpp_source_minus_include: str = handle_stmts(
        src_py.body[i:], ret_imports, ret_h_file, handle_stmt
    )
    h_includes, cpp_includes = calc_includes(ret_imports)
    if cpp_source_minus_include.strip() == "":
        ret_cpp_str = ""
    else:
        all_cpp_includes = f'#include "{h_file}"\n' + cpp_includes
        ret_cpp_str = all_cpp_includes + cpp_source_minus_include
    ret_h_str: str = "#pragma once\n\n" + h_includes + " ".join(ret_h_file)

    return ret_cpp_str, ret_h_str
