import ast
from dataclasses import dataclass


from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.maps.d_types import (
    CustomMappingEntry,
    CustomMappingFromLibEntry,
    CustomMappingStartsWithEntry,
    CustomMappingStartsWithFromLibEntry,
    ToStringEntry,
)
from pypp_cli.src.transpilers.other.transpiler.module.mapping.util import (
    calc_string_fn,
    find_map_entry,
)


@dataclass(frozen=True, slots=True)
class NameHandler:
    _d: Deps

    def handle(self, node: ast.Name) -> str:
        if node.id in self._d.cpp_includes.include_map:
            self._d.add_inc(self._d.cpp_includes.include_map[node.id])
        name: str = node.id
        if name in self._d.user_namespace:
            # In this case there is no need to check the maps, because it wont be in there.
            return "me::" + name

        for k, v in self._d.maps.name.items():
            e = find_map_entry(v, self._d)
            if e is None:
                continue
            if isinstance(e, ToStringEntry):
                if name == k:
                    self._d.add_incs(e.includes)
                    return e.to
            elif isinstance(e, CustomMappingEntry):
                if name == k:
                    self._d.add_incs(e.includes)
                    return e.mapping_fn(node, self._d)
            elif isinstance(e, CustomMappingFromLibEntry):
                if name.startswith(k):
                    self._d.add_incs(e.includes)
                    return calc_string_fn(e)(node, self._d)
            elif isinstance(e, CustomMappingStartsWithEntry):
                if name.startswith(k):
                    self._d.add_incs(e.includes)
                    return e.mapping_fn(node, self._d, name)
            elif isinstance(e, CustomMappingStartsWithFromLibEntry):
                if name.startswith(k):
                    self._d.add_incs(e.includes)
                    return calc_string_fn(e)(node, self._d, name)
        return name
