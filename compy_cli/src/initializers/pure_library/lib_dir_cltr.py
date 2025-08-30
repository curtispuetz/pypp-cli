from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class PureLibDirCltrDeps:
    target_dir: Path


# TODO: move to common location
class PureLibDirCltr:
    def __init__(self, d: PureLibDirCltrDeps):
        self._d = d

    # TODO: remove 'pure' from each method
    def calc_pure_lib_dir(self, lib_dir_name: str) -> Path:
        return self._d.target_dir / lib_dir_name

    def calc_pure_lib_cpp_dir(self, lib_dir_name: str) -> Path:
        return self.calc_pure_lib_dir(lib_dir_name) / "cpp"

    def calc_pure_lib_compy_data_dir(self) -> Path:
        return self._d.target_dir / "compy_data"

    def calc_pure_lib_proj_info(self) -> Path:
        return self.calc_pure_lib_compy_data_dir() / "proj_info.json"

    def calc_pure_lib_timestamps_file(self) -> Path:
        return self.calc_pure_lib_compy_data_dir() / "file_timestamps.json"
