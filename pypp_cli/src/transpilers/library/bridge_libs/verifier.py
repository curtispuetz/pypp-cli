from dataclasses import dataclass
import json
from pathlib import Path

from pydantic import ValidationError
from pypp_cli.src.transpilers.library.bridge_libs.models import BRIDGE_JSON_MODELS
from pypp_cli.src.transpilers.library.bridge_libs.finder import PyppLibs
from pypp_cli.src.transpilers.library.bridge_libs.path_cltr import (
    BridgeJsonPathCltr,
)


def verify_all_bridge_jsons(
    libs: PyppLibs, new_libs: set[str], bridge_json_path_cltr: BridgeJsonPathCltr
):
    did_something: bool = False
    for lib, has_bridge_jsons in libs.items():
        if has_bridge_jsons and lib in new_libs:
            did_something = True
            verifier = _BridgeJsonVerifier(bridge_json_path_cltr, lib)
            verifier.verify_bridge_jsons()
    if did_something:
        print("Verified all bridge JSON files in new libraries")


@dataclass(frozen=True, slots=True)
class _BridgeJsonVerifier:
    _bridge_json_path_cltr: BridgeJsonPathCltr
    _library_name: str

    def verify_bridge_jsons(self):
        # all we have to do is load the jsons into the pydantic models. Pydantic
        # will throw an error if something is wrong.
        for file_name, model in BRIDGE_JSON_MODELS.items():
            json_path: Path = self._bridge_json_path_cltr.calc_bridge_json(
                self._library_name, file_name
            )
            if json_path.exists():
                self._verify_json(json_path, file_name, model)

    def _verify_json(self, json_path: Path, file_name: str, model: type):
        with open(json_path, "r") as f:
            data = json.load(f)
        try:
            model(**data)
        except ValidationError as e:
            raise ValueError(
                f"An issue was found in the {file_name}.json file in "
                f"library {self._library_name}. The issue needs to be fixed in "
                f"the library and then it can be reinstalled. "
                f"The pydantic validation error:"
                f"\n{e}"
            )
