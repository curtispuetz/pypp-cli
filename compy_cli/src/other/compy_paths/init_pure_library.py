from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class InitPureLibraryPaths:
    lib_py_executable: Path
    python_dir: Path
    cpp_dir: Path
    compy_files_dir: Path
    proj_info_file: Path


def create_init_pure_lib_compy_paths(
    target_dir: Path, python_dir_name: str
) -> InitPureLibraryPaths:
    python_dir = target_dir / python_dir_name
    compy_files_dir = target_dir / "compy_files"
    return InitPureLibraryPaths(
        target_dir / ".venv" / "Scripts" / "python.exe",
        python_dir,
        python_dir / "compy_cpp",
        compy_files_dir,
        compy_files_dir / "proj_info.json",
    )
