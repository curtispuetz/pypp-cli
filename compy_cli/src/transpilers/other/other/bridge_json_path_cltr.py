from pathlib import Path


class BridgeJsonPathCltr:
    def __init__(self, site_packages_dir: Path) -> None:
        self._site_packages_dir = site_packages_dir

    def calc_bridge_json(self, library_name: str, json_file_name: str) -> Path:
        return (
            self._site_packages_dir
            / library_name
            / "compy_data"
            / "bridge_jsons"
            / f"{json_file_name}.json"
        )
