from pypp_cli.do.transpile.transpile.z.main_files.single_file_transpiler import (
    MainSingleFileTranspiler,
)
from pypp_cli.do.transpile.transpile.z_i.maps.d_types import Maps

import ast
from dataclasses import dataclass
from pathlib import Path

from pypp_cli.do.transpile.transpile.z.results import TranspileResults


@dataclass(frozen=True, slots=True)
class MainFileTranspiler:
    _namespace: str
    _cpp_dest_dir: Path
    _py_modules: set[str]
    _lib_namespaces: dict[str, str]
    _maps: Maps
    _r: TranspileResults

    def transpile(self, file: Path, file_path: Path, py_ast: ast.Module):
        sf_transpiler = MainSingleFileTranspiler(
            self._namespace,
            self._cpp_dest_dir,
            self._py_modules,
            self._lib_namespaces,
            self._maps,
            self._r,
            file,
            file_path,
            py_ast,
        )
        sf_transpiler.transpile()
