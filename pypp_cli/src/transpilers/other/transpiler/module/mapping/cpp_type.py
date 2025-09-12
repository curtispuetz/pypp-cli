from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.mapping.util import is_imported
from pypp_cli.src.transpilers.other.transpiler.module.util.check_primitive_type import (
    is_primitive_type,
)
from pypp_cli.src.transpilers.other.transpiler.module.util.inner_strings import (
    calc_inside_rd,
)


# Note: It is for types of 1) function parameters and 2) class data members.
def lookup_cpp_type(cpp_arg_type: str, d: Deps) -> str:
    is_pass_by_ref, cpp_arg_type = _is_pass_by_ref(cpp_arg_type, d)
    if cpp_arg_type in d.maps.fn_arg_passed_by_value:
        if is_imported(d.maps.fn_arg_passed_by_value[cpp_arg_type], d):
            return cpp_arg_type
    pass_by_ref_str = "&" if is_pass_by_ref else ""
    before_and_after = cpp_arg_type.split("<", 1)
    if len(before_and_after) == 1:
        return f"{before_and_after[0]}{pass_by_ref_str}"
    before, after = before_and_after
    return f"{before}<{after}{pass_by_ref_str}"


def _is_pass_by_ref(cpp_arg_type: str, d: Deps) -> tuple[bool, str]:
    ret: bool = True
    if cpp_arg_type.startswith("Valu(") and cpp_arg_type.endswith(")"):
        cpp_arg_type = calc_inside_rd(cpp_arg_type)
        if is_primitive_type(cpp_arg_type, d):
            d.value_err_no_ast(
                "Wrapping a primitive type in `Valu()` is not supported since it has "
                "no meaning. Primitive types are always pass-by-value.",
            )
        ret = False
    return ret, cpp_arg_type
