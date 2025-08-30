from pathlib import Path

from compy_cli.src.formatter.format import compy_format
from compy_cli.src.pure_lib_proj_info import load_pure_proj_info
from compy_cli.src.transpiler_pure.transpile import compy_transpile_pure
from compy_cli.src.other.compy_paths.do_pure import (
    DoPureCompyPaths,
    create_do_pure_compy_paths,
)


def compy_do_pure_lib(tasks: list[str], target_dir: Path, exe_name: str | None) -> None:
    proj_info = load_pure_proj_info(target_dir / "compy_files" / "proj_info.json")
    do_helper = _DoPureHelper(
        create_do_pure_compy_paths(target_dir, proj_info.lib_dir_name),
        proj_info.ignored_files,
        exe_name,
    )
    task_methods = {"transpile": do_helper.transpile, "format": do_helper.format}
    for task in tasks:
        assert task in task_methods, "Shouldn't happen"
        task_methods[task]()


class _DoPureHelper:
    def __init__(
        self,
        paths: DoPureCompyPaths,
        ignored_files: list[str],
        exe_name: str | None,
    ):
        self._paths = paths
        self._ignored_files = ignored_files
        self._exe_name = exe_name
        self._files_added_or_modified: list[Path] | None = None

    def transpile(self):
        self._files_added_or_modified = compy_transpile_pure(
            self._paths, self._ignored_files
        )

    def format(self):
        if self._files_added_or_modified is None:
            raise ValueError("'format' can only be specified after 'transpile'")
        compy_format(self._files_added_or_modified, self._paths.cpp_dir)
