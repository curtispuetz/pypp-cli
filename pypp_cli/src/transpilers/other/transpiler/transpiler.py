from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable
from pypp_cli.src.transpilers.other.transpiler.maps.maps import Maps
from pypp_cli.src.transpilers.other.transpiler.main_file import (
    MainFileTranspiler,
)
from pypp_cli.src.transpilers.other.transpiler.results import TranspileResults
from pypp_cli.src.transpilers.other.transpiler.src_file import SrcFileTranspiler


@dataclass(frozen=True, slots=True)
class Transpiler:
    _src_py_files: list[Path]
    _maps: Maps
    _r: TranspileResults = field(default_factory=lambda: TranspileResults([], 0, 0, 0))

    def transpile_all_changed_files(
        self,
        new_files: list[Path],
        changed_files: list[Path],
        py_src_dir: Path,
        cpp_dest_dir: Path,
        is_main_files: bool = False,
    ):
        if is_main_files:
            main_file_transpiler = MainFileTranspiler(
                py_src_dir, cpp_dest_dir, self._src_py_files, self._maps, self._r
            )
            self._transpile_all_changed_files(
                new_files, changed_files, main_file_transpiler.transpile
            )
        else:
            src_file_transpiler = SrcFileTranspiler(
                py_src_dir, cpp_dest_dir, self._src_py_files, self._maps, self._r
            )
            self._transpile_all_changed_files(
                new_files, changed_files, src_file_transpiler.transpile
            )

    def _transpile_all_changed_files(
        self,
        new_files: list[Path],
        changed_files: list[Path],
        fn: Callable[[Path], None],
    ):
        for file in new_files + changed_files:
            self._r.py_files_transpiled += 1
            fn(file)

    def get_results(self) -> TranspileResults:
        return self._r
