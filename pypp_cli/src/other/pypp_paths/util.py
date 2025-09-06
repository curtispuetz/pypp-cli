from pathlib import Path
import sys


def calc_proj_info_path(proj_dir: Path) -> Path:
    return proj_dir / "pypp_files" / "proj_info.json"


def calc_sitepackages_dir(root_dir: Path) -> Path:
    if sys.platform == "win32":
        return root_dir / ".venv" / "Lib" / "site-packages"
    lib_dir = root_dir / ".venv" / "lib"
    python_dirs = [
        d for d in lib_dir.iterdir() if d.is_dir() and d.name.startswith("python")
    ]
    if len(python_dirs) == 0:
        raise FileNotFoundError(f"No python* directory found in {lib_dir}")
    if len(python_dirs) > 1:
        raise FileExistsError(
            f"Multiple python* directories found in {lib_dir}: {python_dirs}"
        )
    return python_dirs[0] / "site-packages"
