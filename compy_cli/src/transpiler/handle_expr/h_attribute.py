import ast

from compy_cli.src.transpiler.deps import Deps
from compy_cli.src.transpiler.mapping.d_types import (
    CustomMappingEntry,
    CustomMappingFromLibEntry,
    CustomMappingStartsWithEntry,
    CustomMappingStartsWithFromLibEntry,
    ReplaceDotWithDoubleColonEntry,
    ToStringEntry,
)
from compy_cli.src.transpiler.mapping.util import calc_string_fn, find_map_entry


def handle_attribute(node: ast.Attribute, d: Deps):
    assert isinstance(node.attr, str), "Not supported"
    attr_str: str = node.attr
    if attr_str == "union":  # This is for the set.union method.
        attr_str += "_"
    value_str = d.handle_expr(node.value)
    if value_str == "self":
        return attr_str
    res = f"{value_str}.{attr_str}"
    for k, v in d.maps.attr.items():
        e = find_map_entry(v, d)
        if e is None:
            continue
        if isinstance(e, ToStringEntry):
            if res == k:
                d.add_incs(e.includes)
                return e.to
        elif isinstance(e, CustomMappingEntry):
            if res == k:
                d.add_incs(e.includes)
                return e.mapping_fn(node, d)
        elif isinstance(e, CustomMappingFromLibEntry):
            if res.startswith(k):
                d.add_incs(e.includes)
                return calc_string_fn(e)(node, d)
        elif isinstance(e, CustomMappingStartsWithEntry):
            if res.startswith(k):
                d.add_incs(e.includes)
                return e.mapping_fn(node, d, res)
        elif isinstance(e, CustomMappingStartsWithFromLibEntry):
            if res.startswith(k):
                d.add_incs(e.includes)
                return calc_string_fn(e)(node, d, res)
        elif isinstance(e, ReplaceDotWithDoubleColonEntry):
            if res.startswith(k):
                d.add_incs(e.includes)
                res = res.replace(".", "::")
                return res
    return res
