from dataclasses import dataclass
from pathlib import Path


@dataclass
class DoPureCompyPaths:
    python_dir: Path
    cpp_dir: Path
    timestamps_file: Path


def create_do_pure_compy_paths(
    target_dir: Path, python_dir_name: str
) -> DoPureCompyPaths:
    python_dir = target_dir / python_dir_name
    compy_files_dir = target_dir / "compy_files"
    return DoPureCompyPaths(
        python_dir, python_dir / "compy_cpp", compy_files_dir / "file_timestamps.json"
    )
