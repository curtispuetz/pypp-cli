import ast

from pypp_cli.do.transpile.transpile.calc_code.z.deps import Deps
from dataclasses import dataclass


# Underscore rules:
# - If the type alias is at module level and does not start with an underscore, then it
# goes in the header file.
# - If the type alias is in a Py++ main file, then it just goes in the main file.


@dataclass(frozen=True, slots=True)
class TypeAliasHandler:
    _d: Deps

    def handle(self, node: ast.TypeAlias, is_module_level: bool = False) -> str:
        if len(node.type_params) != 0:
            self._d.value_err(
                "type parameters for type aliases are not supported", node
            )

        name: str = self._d.handle_expr(node.name)

        is_header_only: bool = is_module_level and not name.startswith("_")

        self._d.set_inc_in_h(is_header_only)
        value: str = self._d.handle_expr(node.value)
        self._d.set_inc_in_h(False)

        res: str = f"using {name} = {value};"
        if is_header_only:
            self._d.ret_h_file.append(res)
            return ""
        return res
