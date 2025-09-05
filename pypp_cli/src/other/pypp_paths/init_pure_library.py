from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class InitPureLibraryPaths:
    python_dir: Path
    cpp_dir: Path
    pypp_files_dir: Path
    proj_info_file: Path


def create_init_pure_lib_pypp_paths(
    target_dir: Path, python_dir_name: str
) -> InitPureLibraryPaths:
    python_dir = target_dir / python_dir_name
    pypp_files_dir = target_dir / "pypp_files"
    return InitPureLibraryPaths(
        python_dir,
        python_dir / "pypp_cpp",
        pypp_files_dir,
        pypp_files_dir / "proj_info.json",
    )
