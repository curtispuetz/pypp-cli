import ast

from pypp_cli.do.y.config import SHOULDNT_HAPPEN
from pypp_cli.do.transpile.transpile.calc_code.z.deps import Deps
from dataclasses import dataclass
from ...util.calc_fn_signature import FnSignatureCalculator


# Underscore rules:
# - If the interface doesn't start with an underscore, then it goes in the header
# file. Otherwise, it goes in the main file.


@dataclass(frozen=True, slots=True)
class InterfaceHandler:
    _d: Deps
    _fn_signature_calculator: FnSignatureCalculator

    def handle(self, node: ast.ClassDef) -> str:
        # Note: interfaces are not supported yet.
        class_name: str = node.name
        is_all_header: bool = not self._d.is_main_file and not class_name.startswith(
            "_"
        )

        self._d.set_inc_in_h(is_all_header)
        body_list = self._calc_methods(node)
        self._d.set_inc_in_h(False)

        body_list.append(_calc_destructor(class_name))
        body_str: str = " ".join(body_list)
        result = f"class {class_name} " + "{" + f"public: {body_str}" + "};\n\n"
        if is_all_header:
            self._d.ret_h_file.append(result)
            return ""
        return result

    def _calc_methods(self, node: ast.ClassDef) -> list[str]:
        ret: list[str] = []
        for item in node.body:
            # Shouldn't happen because Because this was already checked
            assert isinstance(item, ast.FunctionDef), SHOULDNT_HAPPEN
            fn_signature = self._fn_signature_calculator.calc(
                item,
                item.name,
                skip_first_arg=True,  # because it is self
            )
            ret.append("virtual " + fn_signature + " = 0;")
        return ret


def _calc_destructor(class_name: str) -> str:
    # GPT 4.1 recommended that you have a destructor these these 'interface type'
    # classes
    return f"virtual ~{class_name}() " + "{}"
