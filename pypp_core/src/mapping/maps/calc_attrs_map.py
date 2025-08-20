from functools import partial

from pypp_core.src.config import PyppDirs
from pypp_core.src.d_types import QInc, PyImport
from pypp_core.src.mapping.maps.util import (
    calc_map_info,
    load_map,
    calc_common_warning_msg,
)
from pypp_core.src.mapping.info_types import AttrsMap, MapInfo

ATTR_MAP: AttrsMap = {
    "random.Random": {
        PyImport("random"): MapInfo(
            "random::Random",
            [QInc("pypp_random.h")],
        )
    }
}


def calc_attrs_map(proj_info: dict, dirs: PyppDirs) -> AttrsMap:
    return load_map(
        ATTR_MAP,
        proj_info,
        dirs,
        "attrs_map",
        calc_map_info,
        partial(calc_common_warning_msg, name="attribute"),
    )
