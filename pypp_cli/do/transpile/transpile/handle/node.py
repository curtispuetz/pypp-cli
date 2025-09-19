import ast
from pathlib import Path

from pypp_cli.do.transpile.transpile.handle.z.create import create_all_objects
from pypp_cli.do.transpile.transpile.handle.z.deps import Deps
from pypp_cli.do.transpile.transpile.calc_maps.node import Maps
from pypp_cli.do.transpile.transpile.z_i.cpp_includes import CppIncludes
from pypp_cli.do.transpile.transpile.z_i.d_types import QInc
from pypp_cli.do.z_i.config import SHOULDNT_HAPPEN


def _handle_main_stmts(stmts: list[ast.stmt], d: Deps) -> str:
    main_stmt = stmts[-1]
    before_main = d.handle_stmts(stmts[:-1])
    # Shouldnt happen because I already check this
    assert isinstance(main_stmt, ast.If), SHOULDNT_HAPPEN
    inside_main = d.handle_stmts(main_stmt.body + [ast.Return(ast.Constant(0))])
    d.add_inc(QInc("pypp_util/main_error_handler.h"))
    return (
        before_main
        + " int main() { try {"
        + inside_main
        + "} catch (...) { pypp::handle_fatal_exception(); return EXIT_FAILURE;} }"
    )


def calc_code_for_main_file(
    namespace: str,
    py_ast: ast.Module,
    maps: Maps,
    py_modules: set[str],
    lib_namespaces: dict[str, str],
    file_path: Path,
) -> tuple[str, CppIncludes]:
    import_end, d = create_all_objects(
        namespace,
        py_ast,
        maps,
        py_modules,
        lib_namespaces,
        file_path,
        is_main_file=True,
    )
    d.add_inc(QInc("cstdlib"))
    ret = _handle_main_stmts(py_ast.body[import_end:], d)
    return ret, d.cpp_includes


def calc_code_for_src_file(
    namespace: str,
    py_ast: ast.Module,
    maps: Maps,
    py_modules: set[str],
    lib_namespaces: dict[str, str],
    file_path: Path,
) -> tuple[str, CppIncludes, list[str]]:
    import_end, d = create_all_objects(
        namespace,
        py_ast,
        maps,
        py_modules,
        lib_namespaces,
        file_path,
    )
    ret = d.handle_stmts_for_module(py_ast.body[import_end:])
    return ret, d.cpp_includes, d.ret_h_file
