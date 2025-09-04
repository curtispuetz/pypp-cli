from dataclasses import dataclass
from pathlib import Path


@dataclass
class DoPurePyppPaths:
    python_dir: Path
    cpp_dir: Path
    site_packages_dir: Path
    timestamps_file: Path


def create_do_pure_pypp_paths(
    target_dir: Path, python_dir_name: str
) -> DoPurePyppPaths:
    python_dir = target_dir / python_dir_name
    pypp_files_dir = target_dir / "pypp_files"
    return DoPurePyppPaths(
        python_dir,
        python_dir / "pypp_cpp",
        target_dir / ".venv" / "Lib" / "site-packages",
        pypp_files_dir / "file_timestamps.json",
    )
