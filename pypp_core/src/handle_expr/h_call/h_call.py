import ast

from pypp_core.src.deps import Deps
from pypp_core.src.handle_expr.h_starred import handle_call_with_starred_arg
from pypp_core.src.mapping.info_types import (
    CallMapInfo,
    CallMapInfoCppType,
    CallMapInfoCustomMapping,
    CallMapInfoCustomMappingFromLibrary,
    CallMapInfoCustomMappingStartsWith,
    CallMapInfoCustomMappingStartsWithFromLibrary,
    CallMapInfoLeftAndRight,
    CallMapInfoNone,
    CallMapInfoReplaceDotWithDoubleColon,
)


def handle_call(node: ast.Call, d: Deps) -> str:
    assert len(node.keywords) == 0, "keywords for a call are not supported."
    caller_str: str = d.handle_expr(node.func, skip_cpp_lookup=True)
    for _type, info in d.maps.calls.items():
        if isinstance(info, CallMapInfoNone):
            if caller_str == _type and _is_required_import(d, info):
                d.add_incs(info.includes)
                return f"{caller_str}({d.handle_exprs(node.args)})"
        elif isinstance(info, CallMapInfoCppType):
            if caller_str == _type and _is_required_import(d, info):
                d.add_incs(info.includes)
                return f"{info.cpp_type}({d.handle_exprs(node.args)})"
        elif isinstance(info, CallMapInfoLeftAndRight):
            if caller_str == _type and _is_required_import(d, info):
                d.add_incs(info.includes)
                return info.left + d.handle_exprs(node.args) + info.right
        elif isinstance(info, CallMapInfoCustomMapping):
            if caller_str == _type and _is_required_import(d, info):
                d.add_incs(info.includes)
                return info.mapping_fn(node, d)
        elif isinstance(info, CallMapInfoCustomMappingFromLibrary):
            # TODO: implement
            pass
        elif isinstance(info, CallMapInfoCustomMappingStartsWith):
            if caller_str.startswith(_type) and _is_required_import(d, info):
                d.add_incs(info.includes)
                return info.mapping_fn(node, d, caller_str)
        elif isinstance(info, CallMapInfoCustomMappingStartsWithFromLibrary):
            # TODO: implement
            pass
        elif isinstance(info, CallMapInfoReplaceDotWithDoubleColon):
            if caller_str.startswith(_type) and _is_required_import(d, info):
                d.add_incs(info.includes)
                caller_str = caller_str.replace(".", "::")
                return f"{caller_str}({d.handle_exprs(node.args)})"
    return f"{caller_str}({d.handle_exprs(node.args)})"


def _is_required_import(d: Deps, info: CallMapInfo) -> bool:
    return info.required_import is None or d.is_imported(info.required_import)


# TODO later: support starred arguments
def _handle_call_with_starred_arg(
    node: ast.Call, d: Deps, caller_str: str
) -> str | None:
    if len(node.args) == 1:
        first_arg = node.args[0]
        if isinstance(first_arg, ast.Starred):
            assert len(node.args) == 1, (
                "Only one argument is allowed when using a starred argument."
            )
            return handle_call_with_starred_arg(first_arg, d, caller_str)
    return None
