from functools import partial

from compy_cli.src.pypp_dirs import PyppDirs
from compy_cli.src.d_types import QInc, PyImport
from compy_cli.src.mapping.maps.util import (
    calc_map_info,
    load_map,
    calc_common_warning_msg,
)
from compy_cli.src.mapping.info_types import AttrMap, MapInfo

ATTR_MAP: AttrMap = {
    "random.Random": {
        PyImport("random"): MapInfo(
            "random::Random",
            [QInc("compy_random.h")],
        )
    }
}


def calc_attr_map(proj_info: dict, dirs: PyppDirs) -> AttrMap:
    return load_map(
        ATTR_MAP,
        proj_info,
        dirs,
        "attr_map",
        calc_map_info,
        partial(calc_common_warning_msg, name="attribute"),
    )
