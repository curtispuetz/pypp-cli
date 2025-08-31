import ast
from pathlib import Path

from compy_cli.src.transpilers.other.transpiler.deps import Deps
from compy_cli.src.transpilers.other.transpiler.module.handle_expr.expr import (
    handle_expr,
)
from compy_cli.src.transpilers.other.transpiler.module.handle_stmt.stmt import (
    handle_stmt,
)
from compy_cli.src.transpilers.other.transpiler.maps.maps import Maps
from compy_cli.src.transpilers.other.transpiler.handle_import_stmts import (
    analyse_import_stmts,
)
from compy_cli.src.transpilers.other.transpiler.cpp_includes import CppIncludes


def handle_imports_and_create_deps(
    module: ast.Module, maps: Maps, src_py_files: list[Path]
) -> tuple[int, Deps]:
    cpp_inc_map, import_end, py_imports = analyse_import_stmts(
        module.body, maps, src_py_files
    )
    d: Deps = Deps(
        CppIncludes(set(), set(), cpp_inc_map),
        [],
        maps,
        py_imports,
        handle_expr,
        handle_stmt,
    )

    return import_end, d
