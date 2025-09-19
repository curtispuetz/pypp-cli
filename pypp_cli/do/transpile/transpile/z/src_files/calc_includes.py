from pypp_cli.do.transpile.transpile.z.calc_includes import (
    final_result,
)
from pypp_cli.do.transpile.transpile.y.cpp_includes import CppIncludes
from pypp_cli.do.transpile.transpile.z.calc_includes import (
    add_include_to_res,
)


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
    return final_result(ret_h), final_result(ret_cpp)
