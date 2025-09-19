import ast

from pypp_cli.do.transpile.transpile.transpile.z.d_types import QInc
from pypp_cli.do.transpile.transpile.transpile.node import Deps
from pypp_cli.do.transpile.transpile.transpile.z.handlers.mapping.exceptions import (
    lookup_cpp_exception_type,
)
from dataclasses import dataclass

# Underscore rules:
# - If the exception class doesn't start with an underscore, then it goes in the header
# file. Otherwise, it goes in the main file.


_ERR_MSG = "exception class body must only contain 'pass' statement"


@dataclass(frozen=True, slots=True)
class ExceptionClassHandler:
    _d: Deps

    def handle(self, node: ast.ClassDef) -> str:
        class_name = node.name
        err_msg = (
            f"exception class '{class_name}' body must only contain 'pass' statement"
        )
        if len(node.body) != 1:
            self._d.value_err_no_ast(err_msg)
        item = node.body[0]
        if not isinstance(item, ast.Pass):
            self._d.value_err_no_ast(err_msg)
        if len(node.bases) != 1:
            self._d.value_err_no_ast(
                f"exception class '{class_name}' must have exactly one base class"
            )
        base = node.bases[0]
        if not isinstance(base, ast.Name):
            self._d.value_err(
                f"exception class '{class_name}' base class must just be a name", base
            )

        is_all_header: bool = not self._d.is_main_file and not node.name.startswith("_")

        self._d.set_inc_in_h(is_all_header)
        base_name = lookup_cpp_exception_type(base.id, self._d)
        self._d.add_inc(QInc("py_str.h"))
        self._d.set_inc_in_h(False)

        ret = (
            f"class {class_name} : public {base_name}"
            + "{ public: explicit "
            + f"{class_name}(const pypp::PyStr &msg) : {base_name}("
            + f'pypp::PyStr("{class_name}: ") + msg)'
            + "{} };\n\n"
        )
        if is_all_header:
            self._d.ret_h_file.append(ret)
            return ""
        return ret
