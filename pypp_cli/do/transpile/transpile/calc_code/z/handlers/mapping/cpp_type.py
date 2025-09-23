from dataclasses import dataclass
from pypp_cli.do.transpile.transpile.calc_code.z.deps import Deps
from .util import is_imported
from ..util.check_primitive_type import is_primitive_type
from ..util.inner_strings import calc_inside_sq


# Note: It is for types of 1) function parameters and 2) class data members.
@dataclass(frozen=True, slots=True)
class CppTypeCalculator:
    _d: Deps

    def calc(self, cpp_arg_type: str) -> str:
        is_pass_by_ref, cpp_arg_type = self._is_pass_by_ref(cpp_arg_type)
        if cpp_arg_type in self._d.maps.fn_arg_passed_by_value:
            if is_imported(self._d.maps.fn_arg_passed_by_value[cpp_arg_type], self._d):
                return cpp_arg_type
        pass_by_ref_str = "&" if is_pass_by_ref else ""
        before_and_after = cpp_arg_type.split("<", 1)
        if len(before_and_after) == 1:
            return f"{before_and_after[0]}{pass_by_ref_str}"
        before, after = before_and_after
        return f"{before}<{after}{pass_by_ref_str}"

    def _is_pass_by_ref(self, cpp_arg_type: str) -> tuple[bool, str]:
        ret: bool = True
        if cpp_arg_type.startswith("Val[") and cpp_arg_type.endswith("]"):
            cpp_arg_type = calc_inside_sq(cpp_arg_type)
            if is_primitive_type(cpp_arg_type, self._d):
                self._d.value_err_no_ast(
                    "Wrapping a primitive type in `Val[]` is not supported since it "
                    "has no meaning. Primitive types are always pass-by-value.",
                )
            ret = False
        return ret, cpp_arg_type
