from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class InitCompyPaths:
    python_dir: Path
    cpp_dir: Path
    python_src_dir: Path
    resources_dir: Path
    compy_files_dir: Path
    proj_info_file: Path
    py_executable: Path


def create_init_compy_paths(target_dir: Path) -> InitCompyPaths:
    python_dir = target_dir / "python"
    compy_files_dir = target_dir / "compy_files"
    return InitCompyPaths(
        python_dir,
        target_dir / "cpp",
        python_dir / "src",
        target_dir / "resources",
        compy_files_dir,
        compy_files_dir / "proj_info.json",
        python_dir / ".venv" / "Scripts" / "python.exe",
    )
