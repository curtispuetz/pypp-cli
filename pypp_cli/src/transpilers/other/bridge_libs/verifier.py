from dataclasses import dataclass
import json
from pathlib import Path
from typing import Callable
from pypp_cli.src.transpilers.other.other.bridge_json_path_cltr import (
    BridgeJsonPathCltr,
)
from .json_validations.always_pass_by_value import (
    validate_always_pass_by_value,
)
from .json_validations.ann_assign_map import (
    validate_ann_assign_map,
)
from .json_validations.attr_map import (
    validate_attr_map,
)
from .json_validations.call_map import (
    validate_call_map,
)
from .json_validations.cmake_lists import (
    validate_cmake_lists,
)
from .json_validations.import_map import (
    validate_import_map,
)
from .json_validations.name_map import (
    validate_name_map,
)
from .json_validations.subscriptable_types import (
    validate_subscriptable_types,
)


BRIDGE_JSON_VALIDATION: dict[str, Callable[[object], None]] = {
    "name_map": validate_name_map,
    "ann_assign_map": validate_ann_assign_map,
    "import_map": validate_import_map,
    "call_map": validate_call_map,
    "attr_map": validate_attr_map,
    "subscriptable_types": validate_subscriptable_types,
    "always_pass_by_value": validate_always_pass_by_value,
    "cmake_lists": validate_cmake_lists,
}


def verify_all_bridge_libs(
    bridge_libs: list[str], bridge_json_path_cltr: BridgeJsonPathCltr
):
    for bridge_lib in bridge_libs:
        verifier = _BridgeJsonVerifier(bridge_json_path_cltr, bridge_lib)
        verifier.verify_bridge_jsons()
    if len(bridge_libs) > 0:
        print("Verified all JSONS for new bridge-libraries")


@dataclass(frozen=True, slots=True)
class _BridgeJsonVerifier:
    _bridge_json_path_cltr: BridgeJsonPathCltr
    _library_name: str

    def verify_bridge_jsons(self):
        try:
            self._verify_bridge_json_files()
        except AssertionError as e:
            raise AssertionError(
                f"An issue was found in one of the json files for bridge-library "
                f"{self._library_name}: {e}. "
                f"Uninstall {self._library_name}."
            )

    def _verify_bridge_json_files(self):
        for file_name, validate in BRIDGE_JSON_VALIDATION.items():
            json_path: Path = self._bridge_json_path_cltr.calc_bridge_json(
                self._library_name, file_name
            )
            if json_path.exists():
                with open(json_path, "r") as f:
                    data = json.load(f)
                validate(data)
