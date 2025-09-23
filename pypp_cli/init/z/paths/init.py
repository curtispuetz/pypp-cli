from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class InitPyppPaths:
    root_dir: Path
    cpp_dir: Path
    resources_dir: Path
    proj_info_file: Path


def create_init_pypp_paths(target_dir: Path) -> InitPyppPaths:
    pypp = target_dir / ".pypp"
    return InitPyppPaths(
        target_dir,
        pypp / "cpp",
        pypp / "resources",
        pypp / "proj_info.json",
    )
