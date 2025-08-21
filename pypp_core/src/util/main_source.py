import ast
from pathlib import Path

from pypp_core.src.d_types import QInc
from pypp_core.src.deps import Deps, DepsDeps
from pypp_core.src.handle_expr.expr import handle_expr
from pypp_core.src.handle_stmt.stmt import handle_stmt
from pypp_core.src.mapping.maps.maps import Maps
from pypp_core.src.util.calc_includes import calc_includes_for_main_file, calc_includes
from pypp_core.src.util.handle_import_stmts import handle_import_stmts
from pypp_core.src.util.handle_main_stmts import handle_main_stmts
from pypp_core.src.util.ret_imports import RetImports


def calc_main_cpp_source(
    main_py: ast.Module, maps: Maps, src_py_files: list[Path]
) -> str:
    cpp_inc_map, i, py_imports = handle_import_stmts(main_py.body, maps, src_py_files)
    d: Deps = Deps(
        DepsDeps(
            RetImports(set(), set(), cpp_inc_map),
            [],
            py_imports,
            maps,
            handle_expr,
            handle_stmt,
        )
    )
    d.add_inc(QInc("cstdlib"))
    cpp_source_minus_includes: str = handle_main_stmts(main_py.body[i:], d)
    cpp_includes: str = calc_includes_for_main_file(d.ret_imports)
    return cpp_includes + cpp_source_minus_includes


def calc_src_file_cpp_and_h_source(
    src_py: ast.Module, h_file: Path, maps: Maps, src_py_files: list[Path]
) -> tuple[str, str]:
    cpp_inc_map, i, py_imports = handle_import_stmts(src_py.body, maps, src_py_files)
    d: Deps = Deps(
        DepsDeps(
            RetImports(set(), set(), cpp_inc_map),
            [],
            py_imports,
            maps,
            handle_expr,
            handle_stmt,
        )
    )
    cpp_source_minus_include: str = d.handle_stmts(src_py.body[i:])
    h_includes, cpp_includes = calc_includes(d.ret_imports)
    if cpp_source_minus_include.strip() == "":
        ret_cpp_str = ""
    else:
        all_cpp_includes = f'#include "{h_file.as_posix()}"\n' + cpp_includes
        ret_cpp_str = all_cpp_includes + cpp_source_minus_include
    ret_h_str: str = "#pragma once\n\n" + h_includes + " ".join(d.ret_h_file)

    return ret_cpp_str, ret_h_str
