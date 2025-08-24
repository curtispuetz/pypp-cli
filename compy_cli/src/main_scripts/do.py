from pathlib import Path

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.main_scripts.build import compy_build
from compy_cli.src.main_scripts.format import compy_format
from compy_cli.src.main_scripts.run import compy_run
from compy_cli.src.main_scripts.transpile import compy_transpile


def compy_do(tasks: list[str], dirs: CompyDirs, exe_name: str | None) -> None:
    do_helper = _DoHelper(dirs, exe_name)
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
    def __init__(self, dirs: CompyDirs, exe_name: str | None):
        self._dirs = dirs
        self._files_added_or_modified: list[Path] | None = None
        self._exe_name = exe_name

    def transpile(self):
        self._files_added_or_modified = compy_transpile(self._dirs)

    def format(self):
        if self._files_added_or_modified is None:
            raise ValueError("'format' can only be specified after 'transpile'")
        compy_format(self._files_added_or_modified, self._dirs)

    def build(self):
        compy_build(self._dirs)

    def run(self):
        compy_run(self._dirs, self._exe_name)
