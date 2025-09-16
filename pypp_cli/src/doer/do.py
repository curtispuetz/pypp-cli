from dataclasses import dataclass
from pathlib import Path

from pypp_cli.src.builder.build import pypp_build
from pypp_cli.src.config import SHOULDNT_HAPPEN
from pypp_cli.src.formatter.format import pypp_format
from pypp_cli.src.runner.run import pypp_run
from pypp_cli.src.transpilers.proj.transpile import pypp_transpile
from pypp_cli.src.other.pypp_paths.do import DoPyppPaths, create_do_pypp_paths


def pypp_do(tasks: list[str], target_dir: Path, exe_name: str) -> None:
    do_helper = _DoHelper(create_do_pypp_paths(target_dir), exe_name)
    task_methods = {
        "transpile": do_helper.transpile,
        "format": do_helper.format,
        "build": do_helper.build,
        "run": do_helper.run,
    }
    for task in tasks:
        assert task in task_methods, SHOULDNT_HAPPEN
        task_methods[task]()


@dataclass(slots=True)
class _DoHelper:
    _paths: DoPyppPaths
    _exe_name: str
    _files_added_or_modified: list[Path] | None = None

    def transpile(self):
        self._files_added_or_modified = pypp_transpile(self._paths)

    def format(self):
        if self._files_added_or_modified is None:
            raise ValueError("'format' can only be specified after 'transpile'")
        pypp_format(self._files_added_or_modified, self._paths.cpp_dir)

    def build(self):
        pypp_build(self._paths.cpp_dir)

    def run(self):
        pypp_run(self._paths.cpp_build_release_dir, self._exe_name)
