from pathlib import Path


class BridgeJsonPathCltr:
    def __init__(self, py_env_parent_dir) -> None:
        self._py_env_parent_dir = py_env_parent_dir

    def calc_bridge_json(self, library_name: str, json_file_name: str) -> Path:
        return (
            self._py_env_parent_dir
            / ".venv"
            / "Lib"
            / "site-packages"
            / library_name
            / "data"
            / "bridge_jsons"
            / f"{json_file_name}.json"
        )
