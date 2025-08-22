import ast

from pypp_core.src.d_types import QInc
from pypp_core.src.deps import Deps

SPECIAL_CHAR_MAP: dict[int, str] = str.maketrans(
    {
        "\n": "\\n",
        "\t": "\\t",
        "\r": "\\r",
        "\b": "\\b",
        "\f": "\\f",
        "\\": "\\\\",
        '"': '\\"',
    }
)


def handle_constant(node: ast.Constant, d: Deps) -> str:
    if isinstance(node.value, str):
        d.add_inc(QInc("py_str.h"))
        return f'PyStr("{node.value.translate(SPECIAL_CHAR_MAP)}")'
    if isinstance(node.value, bool):
        bool_str = str(node.value)
        first_letter = bool_str[0].lower()
        return first_letter + bool_str[1:]
    if isinstance(node.value, int) or isinstance(node.value, float):
        return str(node.value)
    if node.value is None:
        return "std::monostate"
    raise Exception(f"constant type {node.value} not handled")
