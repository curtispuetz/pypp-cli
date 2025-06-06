from src.d_types import CppInclude, SBInc


def calc_includes_string(ret_imports: set[CppInclude]) -> str:
    ret: list[str] = []
    for imp in ret_imports:
        if isinstance(imp, SBInc):
            ret.append(f"#include <{imp.val}>\n")
        else:
            ret.append(f'#include "{imp.val}"\n')
    return "".join(ret) + "\n"
