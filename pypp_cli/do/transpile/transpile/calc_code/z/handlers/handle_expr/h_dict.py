import ast
from dataclasses import dataclass

from pypp_cli.do.z_i.config import SHOULDNT_HAPPEN
from pypp_cli.do.transpile.transpile.calc_code.z.deps import Deps


@dataclass(frozen=True, slots=True)
class DictHandler:
    _d: Deps

    def handle(self, node: ast.Dict) -> str:
        ret: list[str] = []
        assert len(node.keys) == len(node.values), SHOULDNT_HAPPEN
        for k_node, v_node in zip(node.keys, node.values):
            if k_node is None:
                self._d.value_err_no_ast(
                    "dictionary literals in dict declaration "
                    "(e.g. {0: 1, **a}) not supported "
                )
            k = self._d.handle_expr(k_node)
            v = self._d.handle_expr(v_node)
            ret.append("{" + f"{k}, {v}" + "}")
        return "{" + ", ".join(ret) + "}"
