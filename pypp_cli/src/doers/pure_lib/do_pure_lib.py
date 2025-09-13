from dataclasses import dataclass
from pathlib import Path

from pypp_cli.src.config import SHOULDNT_HAPPEN
from pypp_cli.src.formatter.format import pypp_format
from pypp_cli.src.other.pypp_paths.do_pure import (
    DoPurePyppPaths,
    create_do_pure_pypp_paths,
)
from pypp_cli.src.doers.pure_lib.pure_lib_proj_info import load_pure_proj_info
from pypp_cli.src.other.pypp_paths.util import calc_proj_info_path
from pypp_cli.src.transpilers.pure_lib.transpile import pypp_transpile_pure


def pypp_do_pure_lib(tasks: list[str], target_dir: Path) -> None:
    proj_info = load_pure_proj_info(calc_proj_info_path(target_dir))
    do_helper = _DoPureHelper(
        create_do_pure_pypp_paths(target_dir, proj_info.lib_dir_name),
        proj_info.ignored_files,
    )
    task_methods = {"transpile": do_helper.transpile, "format": do_helper.format}
    for task in tasks:
        assert task in task_methods, SHOULDNT_HAPPEN
        task_methods[task]()


@dataclass(slots=True)
class _DoPureHelper:
    _paths: DoPurePyppPaths
    _ignored_files: list[str]
    _files_added_or_modified: list[Path] | None = None

    def transpile(self):
        self._files_added_or_modified = pypp_transpile_pure(
            self._paths, self._ignored_files
        )

    def format(self):
        if self._files_added_or_modified is None:
            raise ValueError("'format' can only be specified after 'transpile'")
        pypp_format(self._files_added_or_modified, self._paths.cpp_dir)
