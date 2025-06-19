import ast

from src.d_types import CppInclude, QInc


def handle_slice(node: ast.Slice, ret_imports: set[CppInclude], handle_expr):
    ret_imports.add(QInc("py_slice.h"))
    lower: str = "0" if node.lower is None else handle_expr(node.lower, ret_imports)
    step: str = "1" if node.step is None else handle_expr(node.step, ret_imports)
    upper: str = (
        "std::nullopt" if node.upper is None else handle_expr(node.upper, ret_imports)
    )
    return f"PySlice({lower}, {upper}, {step})"
