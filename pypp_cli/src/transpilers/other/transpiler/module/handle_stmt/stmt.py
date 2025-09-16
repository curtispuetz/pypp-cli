import ast
from dataclasses import dataclass

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_ann_assign.h_ann_assign import (  # noqa: E501
    AnnAssignHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_assert import (
    AssertHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_assign import (
    AssignHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_aug_assign import (
    AugAssignHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_class_def.h_class_def import (  # noqa: E501
    ClassDefHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_expr import (
    ExprStmtHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_fn_def import (
    FnDefHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_for import (
    ForHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_if import (
    IfHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_raise import (
    RaiseHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_return import (
    ReturnHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_try import (
    TryHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_type_alias import (
    TypeAliasHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_while import (
    WhileHandler,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_with import (
    WithHandler,
)


@dataclass(frozen=True, slots=True)
class StmtHandler:
    _d: Deps
    assert_handler: AssertHandler
    assign: AssignHandler
    aug_assign: AugAssignHandler
    expr_stmt: ExprStmtHandler
    fn_def: FnDefHandler
    for_handler: ForHandler
    if_handler: IfHandler
    raise_handler: RaiseHandler
    return_handler: ReturnHandler
    try_handler: TryHandler
    type_alias_handler: TypeAliasHandler
    while_handler: WhileHandler
    with_handler: WithHandler
    ann_assign_handler: AnnAssignHandler
    class_def_handler: ClassDefHandler

    def handle(self, node: ast.stmt) -> str:
        if isinstance(node, ast.FunctionDef):
            return self.fn_def.handle(node)
        if isinstance(node, ast.ClassDef):
            return self.class_def_handler.handle(node)
        if isinstance(node, ast.If):
            return self.if_handler.handle(node)
        if isinstance(node, ast.AnnAssign):
            return self.ann_assign_handler.handle(node)
        if isinstance(node, ast.Return):
            return self.return_handler.handle(node)
        if isinstance(node, ast.Assign):
            return self.assign.handle(node)
        if isinstance(node, ast.Expr):
            return self.expr_stmt.handle(node)
        if isinstance(node, ast.AugAssign):
            return self.aug_assign.handle(node)
        if isinstance(node, ast.For):
            return self.for_handler.handle(node)
        if isinstance(node, ast.While):
            return self.while_handler.handle(node)
        if isinstance(node, ast.Break):
            return "break;"
        if isinstance(node, ast.Continue):
            return "continue;"
        if isinstance(node, ast.Raise):
            return self.raise_handler.handle(node)
        if isinstance(node, ast.Try):
            return self.try_handler.handle(node)
        if isinstance(node, ast.With):
            return self.with_handler.handle(node)
        if isinstance(node, ast.Assert):
            return self.assert_handler.handle(node)
        if isinstance(node, ast.TypeAlias):
            return self.type_alias_handler.handle(node)
        if isinstance(node, ast.Pass):
            return ""
        if isinstance(node, (ast.ImportFrom, ast.Import)):
            self._d.value_err(
                "import statements are only supported at the top of the file before "
                "any other code.",
                node,
            )
        self._d.value_err(f"code stmt type {node} not supported", node)
