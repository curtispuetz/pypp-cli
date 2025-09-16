import ast
from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from dataclasses import dataclass

from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_ann_assign.general import (
    GeneralAnnAssignHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_assign import (
    AssignHandler,
)

# Underscore rules:
# - If the config class doesn't start with an underscore, then it goes in the header
# file. Otherwise, it goes in the main file.


@dataclass(frozen=True, slots=True)
class ConfigClassHandler:
    _d: Deps
    _assign_handler: AssignHandler
    _general_ann_assign_handler: GeneralAnnAssignHandler

    def handle(self, node: ast.ClassDef, dtype: ast.expr | None) -> str:
        instance_name: str = node.name
        is_all_header: bool = not self._d.is_main_file and not instance_name.startswith(
            "_"
        )

        self._d.set_inc_in_h(is_all_header)
        body_str: str
        if dtype is None:
            body_str = self._calc_ann_assigns(node)
        else:
            body_str = self._calc_assigns(node, dtype)
        self._d.set_inc_in_h(False)

        # This is a secret name that won't be used other than to create the instance.
        class_name = f"__PseudoPyppName{instance_name}"
        res: str = (
            f"struct {class_name} "
            + "{"
            + body_str
            + "}; "
            + f"inline {class_name} {instance_name};\n\n"
        )
        if is_all_header:
            self._d.ret_h_file.append(res)
            return ""
        return res

    def _calc_ann_assigns(self, node: ast.ClassDef) -> str:
        ret: list[str] = []
        for ann_assign in node.body:
            if not isinstance(ann_assign, ast.AnnAssign):
                self._d.value_err(
                    "A configclass without 'dtype' arg should only have assignments with "
                    "annotations in the class body",
                    ann_assign,
                )
            ret.append(
                self._general_ann_assign_handler.handle(
                    ann_assign, self._d.handle_expr(ann_assign.target)
                )
            )
        return " ".join(ret)

    def _calc_assigns(
        self,
        node: ast.ClassDef,
        dtype: ast.expr,
    ) -> str:
        dtype_str: str = self._d.handle_expr(dtype)
        ret: list[str] = []
        for assign in node.body:
            if not isinstance(assign, ast.Assign):
                self._d.value_err(
                    "A configclass with 'dtype' arg should only have assignments without "
                    "annotations in the class body",
                    assign,
                )
            ret.append(f"{dtype_str} " + self._assign_handler.handle(assign))
        return " ".join(ret)
