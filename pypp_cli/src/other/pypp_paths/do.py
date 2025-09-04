from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class DoPyppPaths:
    proj_info_file: Path
    cpp_dir: Path
    cpp_src_dir: Path
    cpp_build_release_dir: Path
    python_dir: Path
    python_src_dir: Path
    timestamps_file: Path
    site_packages_dir: Path


def create_do_pypp_paths(target_dir: Path) -> DoPyppPaths:
    cpp_dir = target_dir / "cpp"
    cpp_src_dir = cpp_dir / "src"
    cpp_build_release_dir = cpp_dir / "build" / "release"
    python_dir = target_dir / "python"
    python_src_dir = python_dir / "src"
    pypp_files_dir = target_dir / "pypp_files"
    timestamps_file = pypp_files_dir / "file_timestamps.json"
    proj_info_file = pypp_files_dir / "proj_info.json"
    site_packages_dir = python_dir / ".venv" / "Lib" / "site-packages"

    return DoPyppPaths(
        proj_info_file,
        cpp_dir,
        cpp_src_dir,
        cpp_build_release_dir,
        python_dir,
        python_src_dir,
        timestamps_file,
        site_packages_dir,
    )
