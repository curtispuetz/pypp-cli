import ast
from pathlib import Path

from pypp_cli.do.transpile.transpile.z.calc_includes import (
    add_include_to_res,
)
from pypp_cli.do.transpile.transpile.transpile.z.d_types import QInc, header_from_module


def calc_h_code_for_init_file(py_ast: ast.Module, file: Path) -> tuple[str, Path]:
    h_file_name = file.parent
    h_file: Path = h_file_name.with_suffix(".h")
    res: list[str] = ["#pragma once\n\n"]
    for stmt in py_ast.body:
        if _is_assign_with_name_all(stmt):
            continue
        module_name = _validate(stmt)
        add_include_to_res(
            QInc(f"{h_file_name.as_posix()}/{header_from_module(module_name)}"), res
        )
    return "".join(res), h_file


def _validate(stmt: ast.stmt) -> str:
    if not isinstance(stmt, ast.ImportFrom):
        raise ValueError(
            f"Only ImportFrom statements and assigning `__all__` are supported in "
            f"__init__.py files. "
            f"Found:\n{ast.dump(stmt, indent=4)}"
        )
    if stmt.module is None:
        # You can't do `from . import something` because this is importing from a
        # module, and C++ doesn't have that concept.
        raise ValueError(
            f"Only ImportFrom statements with a module are supported in "
            f"__init__.py files. Found:\n{ast.dump(stmt, indent=4)}"
        )
    if stmt.level != 1:
        raise ValueError(
            f"Only ImportFrom statements with a relative import level of 1 "
            f"are supported in __init__.py files. "
            f"Found:\n{ast.dump(stmt, indent=4)}"
        )
    return stmt.module


def _is_assign_with_name_all(stmt: ast.stmt) -> bool:
    if not isinstance(stmt, ast.Assign):
        return False
    if len(stmt.targets) != 1:
        return False
    target: ast.expr = stmt.targets[0]
    if not isinstance(target, ast.Name) or target.id != "__all__":
        return False
    return True
