import ast
from dataclasses import dataclass

from pypp_cli.src.transpilers.other.transpiler.d_types import QInc
from pypp_cli.src.transpilers.other.transpiler.deps import Deps

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


@dataclass(frozen=True, slots=True)
class ConstantHandler:
    _d: Deps

    def handle(self, node: ast.Constant) -> str:
        if isinstance(node.value, str):
            self._d.add_inc(QInc("py_str.h"))
            return f'pypp::PyStr("{node.value.translate(SPECIAL_CHAR_MAP)}")'
        if isinstance(node.value, bool):
            bool_str = str(node.value)
            first_letter = bool_str[0].lower()
            return first_letter + bool_str[1:]
        if isinstance(node.value, int) or isinstance(node.value, float):
            return str(node.value)
        if node.value is None:
            return "std::monostate"
        self._d.value_err(f"constant type {node.value} not supported", node)
