import ast
from dataclasses import dataclass
from typing import Callable

from src.util.ret_imports import RetImports


@dataclass(frozen=True, slots=True)
class Deps:
    ret_imports: RetImports
    ret_h_file: list[str]
    # TODO: use Protocol to define the input args maybe. Or it works now.
    handle_expr_fn: Callable[..., str]
    handle_stmt: Callable[..., str]

    def handle_expr(
        self,
        node: ast.expr,
        include_in_header: bool = False,
        skip_cpp_lookup: bool = False,
    ) -> str:
        return self.handle_expr_fn(node, self, include_in_header, skip_cpp_lookup)
