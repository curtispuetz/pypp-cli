import ast


from compy_cli.src.deps import Deps
from compy_cli.src.mapping.d_types import (
    CustomMappingEntry,
    CustomMappingFromLibEntry,
    CustomMappingStartsWithEntry,
    CustomMappingStartsWithFromLibEntry,
    ToStringEntry,
)
from compy_cli.src.mapping.util import calc_string_fn, find_map_entry


def handle_name(node: ast.Name, d: Deps) -> str:
    if node.id in d.ret_imports.include_map:
        d.add_inc(d.ret_imports.include_map[node.id])
    name: str = node.id

    for k, v in d.maps.name.items():
        e = find_map_entry(v, d)
        if e is None:
            continue
        if isinstance(e, ToStringEntry):
            if name == k:
                d.add_incs(e.includes)
                return e.to
        elif isinstance(e, CustomMappingEntry):
            if name == k:
                d.add_incs(e.includes)
                return e.mapping_fn(node, d)
        elif isinstance(e, CustomMappingFromLibEntry):
            if name.startswith(k):
                d.add_incs(e.includes)
                return calc_string_fn(e, "name_map")(node, d)
        elif isinstance(e, CustomMappingStartsWithEntry):
            if name.startswith(k):
                d.add_incs(e.includes)
                return e.mapping_fn(node, d, k)
        elif isinstance(e, CustomMappingStartsWithFromLibEntry):
            if name.startswith(k):
                d.add_incs(e.includes)
                return calc_string_fn(e, "name_map")(node, d, name)
    return name
