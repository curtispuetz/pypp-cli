import subprocess
from pathlib import Path

from pypp_core.src.pypp_dirs import PyppDirs
from pypp_core.src.util.util import find_file_with_extension


def pip_install_or_uninstall(library: str, dirs: PyppDirs, install: bool) -> str:
    s: str = "install" if install else "uninstall"
    print(f"running 'pip {s}' for library...")
    p = Path(library)
    wheel_file: Path = _find_wheel_file(p)
    subprocess.check_call([dirs.calc_py_executable(), "-m", "pip", s, str(wheel_file)])
    if dirs.timestamps_file.exists():
        dirs.timestamps_file.unlink()
    return p.name


def _find_wheel_file(library: Path) -> Path:
    wheel_file = find_file_with_extension(library / ".." / "dist", "whl")
    if wheel_file is None:
        raise FileNotFoundError(
            f"Could not find a .whl file in the dist/ directory of {library.name}."
        )
    return wheel_file
