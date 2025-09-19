from pypp_cli.do.transpile.transpile.z.other.src_files.single_file_transpiler import (
    SrcSingleFileTranspiler,
)
from pypp_cli.do.transpile.transpile.transpile.z.maps.maps import Maps


import ast
from dataclasses import dataclass
from pathlib import Path

from pypp_cli.do.transpile.transpile.z_i.other.results import TranspileResults


@dataclass(frozen=True, slots=True)
class SrcFileTranspiler:
    _namespace: str
    _cpp_dest_dir: Path
    _py_modules: set[str]
    _lib_namespaces: dict[str, str]
    _maps: Maps
    _r: TranspileResults

    def transpile(self, file: Path, file_path: Path, py_ast: ast.Module):
        sf_transpiler = SrcSingleFileTranspiler(
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
