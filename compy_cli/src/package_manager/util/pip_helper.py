from dataclasses import dataclass
from pathlib import Path
import subprocess


def get_lib_name_and_version_for_whl_file(whl_file: str) -> tuple[str, str]:
    s = Path(whl_file).name.split("-")
    return s[0], s[1]


@dataclass(frozen=True, slots=True)
class PipHelperDeps:
    py_executable: Path
    timestamps_file: Path


class PipHelper:
    def __init__(self, deps: PipHelperDeps):
        self._deps = deps

    def install(self, package: str):
        self._process(package, "install")

    def uninstall(self, package: str):
        self._process(package, "uninstall")

    def _process(self, pip_str: str, s: str):
        print(f"running 'pip {s} {pip_str}'...")
        subprocess.check_call([self._deps.py_executable, "-m", "pip", s, pip_str])
        # Remove timestamps file because changing a library might change how things are
        # transpiled
        if self._deps.timestamps_file.exists():
            self._deps.timestamps_file.unlink()
