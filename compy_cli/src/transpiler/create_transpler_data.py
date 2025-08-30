from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.transpiler.maps.maps import calc_maps
from compy_cli.src.transpiler.util.transpiler import Transpiler, TranspilerDeps


@dataclass(frozen=True, slots=True)
class TranspilerData:
    _transpiler_deps: TranspilerDeps
    transpiler: Transpiler


def create_transpiler_data(
    cpp_dir: Path,
    python_dir: Path,
    cpp_src_dir: Path,
    python_src_dir: Path,
    installed_bridge_libs: dict[str, str],
    src_py_files: list[Path],
) -> TranspilerData:
    transpiler_deps = TranspilerDeps(
        cpp_dir,
        python_dir,
        cpp_src_dir,
        python_src_dir,
        src_py_files,
        calc_maps(installed_bridge_libs, python_dir),
    )
    return TranspilerData(transpiler_deps, Transpiler(transpiler_deps))
