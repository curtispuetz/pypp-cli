from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.transpiler.maps.maps import calc_maps
from compy_cli.src.transpiler.util.transpiler import Transpiler, TranspilerDeps


@dataclass(frozen=True, slots=True)
class TranspilerData:
    _transpiler_deps: TranspilerDeps
    transpiler: Transpiler


def create_transpiler_data(
    dirs: CompyDirs, installed_bridge_libs: dict[str, str], src_py_files: list[Path]
) -> TranspilerData:
    transpiler_deps = TranspilerDeps(
        dirs.cpp_dir,
        dirs.python_dir,
        dirs.cpp_src_dir,
        dirs.python_src_dir,
        src_py_files,
        calc_maps(installed_bridge_libs, dirs.python_dir),
    )
    return TranspilerData(transpiler_deps, Transpiler(transpiler_deps))
