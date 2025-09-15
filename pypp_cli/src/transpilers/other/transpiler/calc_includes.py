from pypp_cli.src.transpilers.other.transpiler.d_types import AngInc, CppInclude
from pypp_cli.src.transpilers.other.transpiler.cpp_includes import CppIncludes


def calc_includes(cpp_includes: CppIncludes) -> tuple[str, str]:
    ret_h: list[str] = []
    for imp in cpp_includes.header:
        add_include_to_res(imp, ret_h)
    ret_cpp: list[str] = []
    for imp in cpp_includes.cpp:
        # There could be duplicates in header and cpp, so check if it is already in the
        #  header.
        if imp not in cpp_includes.header:
            add_include_to_res(imp, ret_cpp)
    return _final_result(ret_h), _final_result(ret_cpp)


def calc_includes_for_main_file(cpp_includes: CppIncludes) -> str:
    ret: list[str] = []
    for imp in cpp_includes.header:
        add_include_to_res(imp, ret)
    for imp in cpp_includes.cpp:
        add_include_to_res(imp, ret)
    return _final_result(ret)


def add_include_to_res(imp: CppInclude, ret: list[str]):
    if isinstance(imp, AngInc):
        ret.append(f"#include <{imp.val}>\n")
    else:
        ret.append(f'#include "{imp.val}"\n')


def _final_result(ret: list[str]) -> str:
    return "".join(ret) + "\n"
