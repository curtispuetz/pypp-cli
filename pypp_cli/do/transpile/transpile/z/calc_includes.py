from pypp_cli.do.transpile.transpile.z_i.d_types import AngInc, CppInclude


def add_include_to_res(imp: CppInclude, ret: list[str]):
    if isinstance(imp, AngInc):
        ret.append(f"#include <{imp.val}>\n")
    else:
        ret.append(f'#include "{imp.val}"\n')


def final_result(ret: list[str]) -> str:
    return "".join(ret) + "\n"
