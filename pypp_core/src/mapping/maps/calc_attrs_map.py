from pypp_core.src.config import PyppDirs
from pypp_core.src.d_types import QInc, PyImport
from pypp_core.src.mapping.maps.util import calc_map_info, load_map
from pypp_core.src.mapping.util import MapInfo

ATTR_MAP: dict[str, MapInfo] = {
    "random.Random": MapInfo(
        "random::Random",
        [QInc("pypp_random.h")],
        PyImport("random"),
    )
}


def calc_attrs_map(proj_info: dict, dirs: PyppDirs) -> dict[str, MapInfo]:
    ret = load_map(ATTR_MAP, proj_info, dirs, "attr", calc_map_info)
    print("attrs_map:")
    print(ret)
    return ret
