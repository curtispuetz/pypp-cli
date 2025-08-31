import ast

from compy_cli.src.transpilers.other.transpiler.d_types import QInc
from compy_cli.src.transpilers.other.transpiler.deps import Deps


def handle_set(node: ast.Set, d: Deps) -> str:
    d.add_inc(QInc("py_set.h"))
    return "PySet({" + d.handle_exprs(node.elts) + "})"
