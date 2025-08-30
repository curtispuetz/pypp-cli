from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.transpiler.maps.maps import calc_maps
from compy_cli.src.transpiler.util.transpiler._helper import TranspilerDeps
from compy_cli.src.transpiler.util.transpiler.transpiler import (
    Transpiler,
)


@dataclass(frozen=True, slots=True)
class TranspilerData:
    _transpiler_deps: TranspilerDeps
    transpiler: Transpiler


def create_transpiler_data(
    python_dir: Path,
    installed_bridge_libs: dict[str, str],
    src_py_files: list[Path],
) -> TranspilerData:
    transpiler_deps = TranspilerDeps(
        src_py_files,
        calc_maps(installed_bridge_libs, python_dir),
    )
    return TranspilerData(transpiler_deps, Transpiler(transpiler_deps))
