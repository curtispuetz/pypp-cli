from dataclasses import dataclass
from typing import Callable

from pypp_cli.src.transpilers.library.transpiler.d_types import (
    PySpecificImport,
)
from pypp_cli.src.transpilers.library.transpiler.maps.util.type_2.helper import (
    MapCltr2Helper,
)
from pypp_cli.src.transpilers.library.transpiler.maps.util.util import (
    MapCltrAlgo,
)


@dataclass(frozen=True, slots=True)
class MapCltr2(MapCltrAlgo):
    type Map = dict[str, set[PySpecificImport | None]]

    def calc_map_2(
        self,
        default_map: Map,
        json_file_name: str,
        warning_fn: Callable[[str, str], str],
    ) -> Map:
        helper = MapCltr2Helper(
            self._libs,
            self._bridge_json_path_cltr,
            default_map,
            json_file_name,
            warning_fn,
        )
        return helper.calc()
