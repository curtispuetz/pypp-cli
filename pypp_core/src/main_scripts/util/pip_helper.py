import subprocess
from pathlib import Path

from pypp_core.src.pypp_dirs import PyppDirs
from pypp_core.src.util.util import find_file_with_extension


def pip_install(library: str, dirs: PyppDirs) -> str:
    return _process(library, dirs, "install")


def pip_uninstall(library: str, dirs: PyppDirs) -> str:
    return _process(library, dirs, "uninstall")


def _process(library: str, dirs: PyppDirs, s: str) -> str:
    print(f"running 'pip {s}' for library...")
    p = Path(library)
    wheel_file: str = _find_wheel_file(library)
    subprocess.check_call([dirs.calc_py_executable(), "-m", "pip", s, wheel_file])
    # Remove timestamps file because changing a library might change how things are
    # transpiled
    if dirs.timestamps_file.exists():
        dirs.timestamps_file.unlink()
    return p.name


def _find_wheel_file(library: str) -> str:
    p = Path(library)
    wheel_file = find_file_with_extension(p / ".." / "dist", "whl")
    if wheel_file is None:
        raise FileNotFoundError(
            f"Could not find a .whl file in the dist/ directory of {p.name}."
        )
    return str(wheel_file)
