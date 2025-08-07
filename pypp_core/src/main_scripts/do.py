from pathlib import Path

from pypp_core.src.config import PyppDirs
from pypp_core.src.main_scripts.build import pypp_build
from pypp_core.src.main_scripts.format import pypp_format
from pypp_core.src.main_scripts.run import pypp_run
from pypp_core.src.main_scripts.transpile import pypp_transpile


def pypp_do(tasks: list[str], dirs: PyppDirs) -> None:
    do_helper = _DoHelper(dirs)
    task_methods = {
        "transpile": do_helper.transpile,
        "format": do_helper.format,
        "build": do_helper.build,
        "run": do_helper.run,
    }
    for task in tasks:
        assert task in task_methods, "Shouldn't happen"
        task_methods[task]()

class _DoHelper:
    def __init__(self, dirs: PyppDirs):
        self._dirs = dirs
        self._files_added_or_modified: list[Path] | None = None

    def transpile(self):
        self._files_added_or_modified = pypp_transpile(self._dirs)

    def format(self):
        if self._files_added_or_modified is None:
            raise ValueError("'format' can only be specified after 'transpile'")
        pypp_format(self._files_added_or_modified, self._dirs)

    def build(self):
        pypp_build(self._dirs)

    def run(self):
        pypp_run(self._dirs)
