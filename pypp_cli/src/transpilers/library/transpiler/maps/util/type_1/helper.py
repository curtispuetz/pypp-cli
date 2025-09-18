from dataclasses import dataclass
import json
from pathlib import Path
from typing import Callable

from pypp_cli.src.transpilers.library.transpiler.d_types import PySpecificImport
from pypp_cli.src.transpilers.library.transpiler.maps.util.util import (
    MapCltrAlgo,
    calc_imp_str,
    calc_required_py_import,
)


@dataclass(frozen=True, slots=True)
class MapCltr1Helper[T](MapCltrAlgo):
    type Map = dict[str, dict[PySpecificImport | None, T]]
    _base_map: Map
    _calc_entry_fn_map: dict[str, Callable[[dict], T]]
    _json_file_name: str
    _friendly_name: str

    def calc(self) -> Map:
        ret = self._base_map.copy()
        for lib, has_bridge_jsons in self._libs.items():
            if not has_bridge_jsons:
                continue
            json_path: Path = self._bridge_json_path_cltr.calc_bridge_json(
                lib, self._json_file_name
            )
            if not json_path.is_file():
                continue
            self._calc_for_lib(json_path, lib, ret)
        # Check for extra map in .pypp/bridge_jsons
        file = self._proj_bridge_json_dir / f"{self._json_file_name}.json"
        if file.is_file():
            # TODO: add verification for the file.
            self._calc_for_lib(file, None, ret)
        return ret

    def _calc_for_lib(self, json_path: Path, lib: str | None, ret: Map):
        # TODO: instead of loading the json here again, I should just
        # hold them from the place where I verified them and loaded them as
        # pydantic models.
        with open(json_path, "r") as f:
            m: dict = json.load(f)
        for mapping_type, obj in m.items():
            if lib is None:
                self._assert_valid_mapping_type_local(mapping_type)
            else:
                self._assert_valid_mapping_type(mapping_type, lib)
            self._calc_for_mapping_type(mapping_type, obj, lib, ret)

    def _calc_for_mapping_type(
        self, mapping_type: str, obj: dict, lib: str | None, ret: Map
    ):
        for k, v in obj.items():
            required_import = calc_required_py_import(v)
            if k in ret:
                if required_import in ret[k]:
                    if lib is None:
                        self._override_mapping_warning_local(k, required_import)
                    else:
                        self._override_mapping_warning(k, required_import, lib)
                ret[k][required_import] = self._calc_entry_fn_map[mapping_type](v)
            else:
                ret[k] = {required_import: self._calc_entry_fn_map[mapping_type](v)}

    def _assert_valid_mapping_type(self, mapping_type: str, lib: str):
        assert mapping_type in self._calc_entry_fn_map, (
            f"invalid key '{mapping_type}' in {self._json_file_name}.json for "
            f"'{lib}' library. "
            f"This shouldn't happen because the json should be "
            f"validated when the library is installed"
        )

    def _assert_valid_mapping_type_local(self, mapping_type: str):
        assert mapping_type in self._calc_entry_fn_map, (
            f"invalid key '{mapping_type}' in {self._json_file_name}.json"
        )

    def _override_mapping_warning(
        self, k: str, required_import: PySpecificImport | None, lib: str
    ):
        print(
            f"warning: Py++ transpiler already maps the "
            f"{self._friendly_name} "
            f"'{k}{calc_imp_str(required_import)}'. Library "
            f"{lib} is overriding this mapping."
        )

    def _override_mapping_warning_local(
        self, k: str, required_import: PySpecificImport | None
    ):
        print(
            f"warning: Py++ transpiler already maps the "
            f"{self._friendly_name} "
            f"'{k}{calc_imp_str(required_import)}'. The "
            f".pypp/bridge_jsons/{self._json_file_name}.json is overriding this "
            f"mapping."
        )
