import ast

from pypp_cli.do.y.config import SHOULDNT_HAPPEN
from pypp_cli.do.transpile.transpile.y.d_types import (
    QInc,
    PyImp,
    AngInc,
)
from pypp_cli.do.transpile.transpile.y.maps.d_types import (
    LeftAndRightEntry,
    CallMap,
    ToStringEntry,
    CustomMappingEntry,
    CustomMappingStartsWithEntry,
)
from pypp_cli.do.transpile.transpile.calc_maps.z.call.default_dict_map_fn import (
    good_default_dict,
)


def _default_dict(_node: ast.Call, d) -> str:
    d.value_err_no_ast(
        "defaultdict must be called with type info "
        "(i.e. defaultdict[KeyType, ValueType])"
    )
    return SHOULDNT_HAPPEN


def _2_arg_helper(node: ast.Call, d, name: str, middle: str, end: str) -> str:
    assert len(node.args) == 2, f"{name} should have 2 arguments"
    arg1 = d.handle_expr(node.args[0])
    arg2 = d.handle_expr(node.args[1])
    return f"{arg1}.{middle}{arg2}{end}"


def _tuple_get(node: ast.Call, d) -> str:
    return _2_arg_helper(node, d, "tg", "get<", ">()")


def _dict_get(node: ast.Call, d) -> str:
    return _2_arg_helper(node, d, "dg", "dg(", ")")


def _list_get(node: ast.Call, d) -> str:
    return _2_arg_helper(node, d, "lg", "lg(", ")")


def _union_get(node: ast.Call, d) -> str:
    return _2_arg_helper(node, d, "ug", "ug<", ">()")


def _union_isinst(node: ast.Call, d) -> str:
    return _2_arg_helper(node, d, "isinst", "isinst<", ">()")


def _union_is_none(node: ast.Call, d) -> str:
    assert len(node.args) == 1, "is_none should have 1 argument"
    obj_arg = d.handle_expr(node.args[0])
    return f"{obj_arg}.is_none()"


def _list_reserve(node: ast.Call, d) -> str:
    return _2_arg_helper(node, d, "list_reserve", "reserve(", ")")


def _pypp_time(node: ast.Call, d, caller_str: str) -> str:
    fn: str = caller_str[caller_str.rfind(".") + 1 :]
    return f"pypp::time::{fn}({d.handle_exprs(node.args)})"


def _replace_dot_with_double_colon(node: ast.Call, d, caller_str: str) -> str:
    caller_str = caller_str.replace(".", "::")
    return f"pypp::{caller_str}({d.handle_exprs(node.args)})"


CALL_MAP: CallMap = {
    "print": {None: ToStringEntry("pypp::print", [QInc("pypp_util/print.h")])},
    "len": {None: LeftAndRightEntry("", ".len()", [])},
    "min": {None: LeftAndRightEntry("", ".min()", [])},
    "max": {None: LeftAndRightEntry("", ".max()", [])},
    "to_std_string": {
        PyImp("pypp_python", "to_std_string"): LeftAndRightEntry("", ".str()", [])
    },
    "to_c_string": {
        PyImp("pypp_python", "to_c_string"): LeftAndRightEntry("", ".str().c_str()", [])
    },
    "pypp::PyList": {
        None: ToStringEntry("pypp::list", [QInc("pypp_util/create/list.h")])
    },
    "pypp::PyDict": {
        None: ToStringEntry("pypp::dict", [QInc("pypp_util/create/dict.h")])
    },
    "pypp::PySet": {None: ToStringEntry("pypp::set", [QInc("pypp_util/create/set.h")])},
    "pypp::PyStr": {None: ToStringEntry("pypp::str", [QInc("pypp_util/to_py_str.h")])},
    "bool": {None: ToStringEntry("pypp::bool_", [QInc("pypp_util/create/others.h")])},
    "int": {None: ToStringEntry("pypp::int_", [QInc("pypp_util/create/others.h")])},
    "to_float32": {
        PyImp("pypp_python", "float32"): ToStringEntry(
            "pypp::to_float32", [QInc("pypp_util/create/others.h")]
        )
    },
    "double": {
        None: ToStringEntry("pypp::float_", [QInc("pypp_util/create/others.h")])
    },
    "to_int8_t": {
        PyImp("pypp_python", "to_int8_t"): ToStringEntry(
            "pypp::to_int8_t", [QInc("pypp_util/create/cstdint.h")]
        )
    },
    "to_int16_t": {
        PyImp("pypp_python", "to_int16_t"): ToStringEntry(
            "pypp::to_int16_t", [QInc("pypp_util/create/cstdint.h")]
        )
    },
    "to_int32_t": {
        PyImp("pypp_python", "to_int32_t"): ToStringEntry(
            "pypp::to_int32_t", [QInc("pypp_util/create/cstdint.h")]
        )
    },
    "to_int64_t": {
        PyImp("pypp_python", "to_int64_t"): ToStringEntry(
            "pypp::to_int64_t", [QInc("pypp_util/create/cstdint.h")]
        )
    },
    "to_uint8_t": {
        PyImp("pypp_python", "to_uint8_t"): ToStringEntry(
            "pypp::to_uint8_t", [QInc("pypp_util/create/cstdint.h")]
        )
    },
    "to_uint16_t": {
        PyImp("pypp_python", "to_uint16_t"): ToStringEntry(
            "pypp::to_uint16_t", [QInc("pypp_util/create/cstdint.h")]
        )
    },
    "to_uint32_t": {
        PyImp("pypp_python", "to_uint32_t"): ToStringEntry(
            "pypp::to_uint32_t", [QInc("pypp_util/create/cstdint.h")]
        )
    },
    "to_uint64_t": {
        PyImp("pypp_python", "to_uint64_t"): ToStringEntry(
            "pypp::to_uint64_t", [QInc("pypp_util/create/cstdint.h")]
        )
    },
    "pypp::PySlice": {
        None: ToStringEntry("pypp::py_slice", [QInc("slice/creators.h")])
    },
    "mov": {
        PyImp("pypp_python", "mov"): ToStringEntry("std::move", [AngInc("utility")])
    },
    "res_dir": {
        PyImp("pypp_python", "res_dir"): ToStringEntry(
            "pypp::res_dir", [QInc("pypp_resources.h")]
        )
    },
    "int_pow": {
        PyImp("pypp_python", "int_pow"): ToStringEntry(
            "pypp::int_pow", [QInc("pypp_util/math.h")]
        )
    },
    "pypp::PyDefaultDict": {
        PyImp("pypp_python", "defaultdict"): CustomMappingEntry(_default_dict, [])
    },
    "tg": {PyImp("pypp_python", "tg"): CustomMappingEntry(_tuple_get, [])},
    "dg": {PyImp("pypp_python", "dg"): CustomMappingEntry(_dict_get, [])},
    "lg": {PyImp("pypp_python", "lg"): CustomMappingEntry(_list_get, [])},
    "ug": {PyImp("pypp_python", "ug"): CustomMappingEntry(_union_get, [])},
    "isinst": {PyImp("pypp_python", "isinst"): CustomMappingEntry(_union_isinst, [])},
    "is_none": {
        PyImp("pypp_python", "is_none"): CustomMappingEntry(_union_is_none, [])
    },
    "list_reserve": {
        PyImp("pypp_python", "list_reserve"): CustomMappingEntry(_list_reserve, [])
    },
    "pypp::PyDefaultDict<": {
        PyImp("pypp_python", "defaultdict"): CustomMappingStartsWithEntry(
            good_default_dict, []
        )
    },
    "os.": {
        PyImp("pypp_python.stl", "os"): CustomMappingStartsWithEntry(
            _replace_dot_with_double_colon, [QInc("pypp_os.h")]
        )
    },
    "shutil.": {
        PyImp("pypp_python.stl", "shutil"): CustomMappingStartsWithEntry(
            _replace_dot_with_double_colon, [QInc("pypp_shutil.h")]
        )
    },
    "time.": {
        PyImp("pypp_python.stl", "time"): CustomMappingStartsWithEntry(
            _pypp_time, [QInc("pypp_time.h")]
        )
    },
}
