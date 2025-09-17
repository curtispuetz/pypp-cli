from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class BridgeJsonPathCltr:
    _site_packages_dir: Path

    def calc_bridge_json(self, library_name: str, json_file_name: str) -> Path:
        return (
            self._site_packages_dir
            / library_name
            / ".pypp"
            / "bridge_jsons"
            / f"{json_file_name}.json"
        )
