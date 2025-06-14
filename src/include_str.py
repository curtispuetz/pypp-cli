from src.d_types import CppInclude, SBInc


def calc_includes_string(ret_imports: set[CppInclude]) -> str:
    ret: list[str] = []
    for imp in ret_imports:
        if isinstance(imp, SBInc):
            ret.append(f"#include <{imp.val}>\n")
        else:
            # TODO later: these specific strings should be different in the future
            #  once I figure out how to deal with the custom Py++ Python code there
            if imp.val.startswith("test_dir/python/pypp/"):
                continue
            ret.append(f'#include "{imp.val}"\n')
    return "".join(ret) + "\n"
