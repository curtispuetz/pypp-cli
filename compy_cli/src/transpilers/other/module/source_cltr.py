import ast
from pathlib import Path

from compy_cli.src.transpilers.other.module.d_types import QInc
from compy_cli.src.transpilers.other.module.deps import Deps
from compy_cli.src.transpilers.other.module.handle_expr.expr import handle_expr
from compy_cli.src.transpilers.other.module.handle_stmt.stmt import handle_stmt
from compy_cli.src.transpilers.other.maps.maps import Maps
from compy_cli.src.transpilers.other.module.util.calc_includes import (
    calc_includes_for_main_file,
    calc_includes,
)
from compy_cli.src.transpilers.other.module.util.handle_import_stmts import (
    handle_import_stmts,
)
from compy_cli.src.transpilers.other.module.util.handle_main_stmts import (
    handle_main_stmts,
)
from compy_cli.src.transpilers.other.module.util.ret_imports import RetImports


# TODO: this code is confusing. Should make it make more sense by renaming things.
def calc_main_cpp_source(
    main_py: ast.Module, maps: Maps, src_py_files: list[Path]
) -> str:
    i, d = _create_deps(main_py, maps, src_py_files)
    d.add_inc(QInc("cstdlib"))
    cpp_source_minus_includes: str = handle_main_stmts(main_py.body[i:], d)
    cpp_includes: str = calc_includes_for_main_file(d.ret_imports)
    return cpp_includes + cpp_source_minus_includes


def calc_src_file_cpp_and_h_source(
    src_py: ast.Module, h_file: Path, maps: Maps, src_py_files: list[Path]
) -> tuple[str, str]:
    i, d = _create_deps(src_py, maps, src_py_files)
    cpp_source_minus_include: str = d.handle_stmts(src_py.body[i:])
    h_includes, cpp_includes = calc_includes(d.ret_imports)
    if cpp_source_minus_include.strip() == "":
        ret_cpp_str = ""
    else:
        all_cpp_includes = f'#include "{h_file.as_posix()}"\n' + cpp_includes
        ret_cpp_str = all_cpp_includes + cpp_source_minus_include
    ret_h_str: str = "#pragma once\n\n" + h_includes + " ".join(d.ret_h_file)

    return ret_cpp_str, ret_h_str


def _create_deps(
    module: ast.Module, maps: Maps, src_py_files: list[Path]
) -> tuple[int, Deps]:
    cpp_inc_map, i, py_imports = handle_import_stmts(module.body, maps, src_py_files)
    d: Deps = Deps(
        RetImports(set(), set(), cpp_inc_map),
        [],
        maps,
        py_imports,
        handle_expr,
        handle_stmt,
    )

    return i, d
