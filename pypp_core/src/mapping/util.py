from pypp_core.src.d_types import PySpecificImport
from pypp_core.src.deps import Deps


def is_one(r: dict[PySpecificImport | None, None], d: Deps) -> bool:
    if None in r:
        return True
    for required_import in r.keys():
        if required_import is not None and d.is_imported(required_import):
            return True
    return False


def find_map_info[T](r: dict[PySpecificImport | None, T], d: Deps) -> T | None:
    for required_import, map_info in r.items():
        if required_import is not None and d.is_imported(required_import):
            return map_info
    if None in r:
        return r[None]
    return None
