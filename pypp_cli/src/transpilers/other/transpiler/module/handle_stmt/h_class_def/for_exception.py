import ast

from pypp_cli.src.transpilers.other.transpiler.d_types import QInc
from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.mapping.exceptions import (
    lookup_cpp_exception_type,
)

# Underscore rules:
# - If the exception class doesn't start with an underscore, then it goes in the header
# file. Otherwise, it goes in the main file.


_ERR_MSG = "exception class body must only contain 'pass' statement"


def handle_class_def_for_exception(
    node: ast.ClassDef,
    d: Deps,
) -> str:
    class_name = node.name
    err_msg = f"exception class '{class_name}' body must only contain 'pass' statement"
    if len(node.body) != 1:
        d.value_err_no_ast(err_msg)
    item = node.body[0]
    if not isinstance(item, ast.Pass):
        d.value_err_no_ast(err_msg)
    if len(node.bases) != 1:
        d.value_err_no_ast(
            f"exception class '{class_name}' must have exactly one base class"
        )
    base = node.bases[0]
    if not isinstance(base, ast.Name):
        d.value_err(
            f"exception class '{class_name}' base class must just be a name", base
        )

    is_all_header: bool = not d.is_main_file and not node.name.startswith("_")

    d.set_inc_in_h(is_all_header)
    base_name = lookup_cpp_exception_type(base.id, d)
    d.add_inc(QInc("py_str.h"))
    d.set_inc_in_h(False)

    ret = (
        f"class {class_name} : public {base_name}"
        + "{ public: explicit "
        + f"{class_name}(const pypp::PyStr &msg) : {base_name}("
        + f'pypp::PyStr("{class_name}: ") + msg)'
        + "{} };\n\n"
    )
    if is_all_header:
        d.ret_h_file.append(ret)
        return ""
    return ret
