import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.calc_code.z.deps import Deps
from pypp_cli.do.transpile.transpile.z_i.maps.d_types import (
    CustomMappingEntry,
    CustomMappingFromLibEntry,
    CustomMappingStartsWithEntry,
    CustomMappingStartsWithFromLibEntry,
    ReplaceDotWithDoubleColonEntry,
    ToStringEntry,
)
from pypp_cli.do.transpile.transpile.calc_code.z.handlers.mapping.util import (
    calc_string_fn,
    find_map_entry,
)


@dataclass(frozen=True, slots=True)
class AttributeHandler:
    _d: Deps

    def handle(self, node: ast.Attribute) -> str:
        attr_str: str = node.attr
        if attr_str == "union":  # This is for the set.union method.
            attr_str += "_"
        value_str = self._d.handle_expr(node.value)
        if value_str == "self":
            return attr_str
        res = f"{value_str}.{attr_str}"
        for k, v in self._d.maps.attr.items():
            e = find_map_entry(v, self._d)
            if e is None:
                continue
            if isinstance(e, ToStringEntry):
                if res == k:
                    self._d.add_incs(e.includes)
                    return e.to
            elif isinstance(e, CustomMappingEntry):
                if res == k:
                    self._d.add_incs(e.includes)
                    return e.mapping_fn(node, self._d)
            elif isinstance(e, CustomMappingFromLibEntry):
                if res.startswith(k):
                    self._d.add_incs(e.includes)
                    return calc_string_fn(e)(node, self._d)
            elif isinstance(e, CustomMappingStartsWithEntry):
                if res.startswith(k):
                    self._d.add_incs(e.includes)
                    return e.mapping_fn(node, self._d, res)
            elif isinstance(e, CustomMappingStartsWithFromLibEntry):
                if res.startswith(k):
                    self._d.add_incs(e.includes)
                    return calc_string_fn(e)(node, self._d, res)
            elif isinstance(e, ReplaceDotWithDoubleColonEntry):
                if res.startswith(k):
                    self._d.add_incs(e.includes)
                    res = res.replace(".", "::")
                    if e.add_pypp_namespace:
                        res = "pypp::" + res
                    return res
        return res
