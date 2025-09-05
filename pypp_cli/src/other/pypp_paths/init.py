from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class InitPyppPaths:
    python_dir: Path
    cpp_dir: Path
    python_src_dir: Path
    resources_dir: Path
    pypp_files_dir: Path
    proj_info_file: Path


def create_init_pypp_paths(target_dir: Path) -> InitPyppPaths:
    python_dir = target_dir / "python"
    pypp_files_dir = target_dir / "pypp_files"
    return InitPyppPaths(
        python_dir,
        target_dir / "cpp",
        python_dir / "src",
        target_dir / "resources",
        pypp_files_dir,
        pypp_files_dir / "proj_info.json",
    )
