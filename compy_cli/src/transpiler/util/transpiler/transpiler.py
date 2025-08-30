from dataclasses import dataclass
from pathlib import Path
from compy_cli.src.transpiler.util.transpiler._helper import (
    TranspilerDeps,
    TranspilerHelper,
)


@dataclass
class TranspileResults:
    files_added_or_modified: list[Path]
    py_files_transpiled: int
    header_files_written: int
    cpp_files_written: int


class Transpiler:
    def __init__(self, d: TranspilerDeps) -> None:
        self._d = d
        self._helper = TranspilerHelper(self._d)

    def transpile_all_changed_files(
        self,
        new_files: list[Path],
        changed_files: list[Path],
        py_dir: Path,
        cpp_dir: Path,
        is_main_files: bool = False,
    ):
        self._helper.transpile_all_changed_files(
            new_files, changed_files, py_dir, cpp_dir, is_main_files
        )

    def get_results(self) -> TranspileResults:
        return TranspileResults(
            self._helper.files_added_or_modified,
            self._helper.py_files_transpiled,
            self._helper.header_files_written,
            self._helper.cpp_files_written,
        )
