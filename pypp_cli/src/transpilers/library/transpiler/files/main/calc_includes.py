from pypp_cli.src.transpilers.library.transpiler.files.util.calc_includes import (
    final_result,
)
from pypp_cli.src.transpilers.library.transpiler.cpp_includes import CppIncludes
from pypp_cli.src.transpilers.library.transpiler.files.util.calc_includes import (
    add_include_to_res,
)


def calc_includes_for_main_file(cpp_includes: CppIncludes) -> str:
    ret: list[str] = []
    for imp in cpp_includes.header:
        add_include_to_res(imp, ret)
    for imp in cpp_includes.cpp:
        add_include_to_res(imp, ret)
    return final_result(ret)
