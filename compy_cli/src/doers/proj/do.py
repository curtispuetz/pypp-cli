from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.builder.build import compy_build
from compy_cli.src.formatter.format import compy_format
from compy_cli.src.runner.run import compy_run
from compy_cli.src.transpilers.proj.transpile import compy_transpile
from compy_cli.src.other.compy_paths.do import DoCompyPaths, create_do_compy_paths


def compy_do(tasks: list[str], target_dir: Path, exe_name: str | None) -> None:
    do_helper = _DoHelper(create_do_compy_paths(target_dir), exe_name)
    task_methods = {
        "transpile": do_helper.transpile,
        "format": do_helper.format,
        "build": do_helper.build,
        "run": do_helper.run,
    }
    for task in tasks:
        assert task in task_methods, "Shouldn't happen"
        task_methods[task]()


@dataclass(slots=True)
class _DoHelper:
    _paths: DoCompyPaths
    _exe_name: str
    _files_added_or_modified: list[Path] | None = None

    def transpile(self):
        self._files_added_or_modified = compy_transpile(self._paths)

    def format(self):
        if self._files_added_or_modified is None:
            raise ValueError("'format' can only be specified after 'transpile'")
        compy_format(self._files_added_or_modified, self._paths.cpp_dir)

    def build(self):
        compy_build(self._paths.cpp_dir)

    def run(self):
        compy_run(self._paths.cpp_build_release_dir, self._exe_name)
