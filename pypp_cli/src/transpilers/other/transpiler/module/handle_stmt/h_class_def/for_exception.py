import ast

from pypp_cli.src.transpilers.other.transpiler.d_types import QInc
from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.mapping.exceptions import (
    lookup_cpp_exception_type,
)


def handle_class_def_for_exception(
    node: ast.ClassDef,
    d: Deps,
) -> str:
    err_msg = "exception class body must only contain 'pass' statement"
    assert len(node.body) == 1, err_msg
    item = node.body[0]
    assert isinstance(item, ast.Pass), err_msg
    assert len(node.bases) == 1, "exception class must have exactly one base class"
    base = node.bases[0]
    assert isinstance(base, ast.Name), "exception class base must be a Name"
    name_doesnt_start_with_underscore: bool = not node.name.startswith("_")
    d.set_inc_in_h(name_doesnt_start_with_underscore)
    base_name = lookup_cpp_exception_type(base.id, d)
    d.add_inc(QInc("py_str.h"))
    d.set_inc_in_h(False)
    class_name = node.name
    ret = (
        f"class {class_name} : public {base_name}"
        + "{ public: explicit "
        + f"{class_name}(const PyStr &msg) : {base_name}("
        + f'PyStr("{class_name}: ") + msg)'
        + "{} };\n\n"
    )
    if name_doesnt_start_with_underscore:
        d.ret_h_file.append(ret)
        return ""
    return ret
