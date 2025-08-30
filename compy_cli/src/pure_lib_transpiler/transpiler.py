from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.transpiler.bridge_json_path_cltr import BridgeJsonPathCltr
from compy_cli.src.transpiler.bridge_libs.finder import find_bridge_libs
from compy_cli.src.transpiler.bridge_libs.verifier import verify_all_bridge_libs
from compy_cli.src.transpiler.create_transpler_data import create_transpiler
from compy_cli.src.transpiler.print_results import print_transpilation_results
from compy_cli.src.transpiler.util.file_changes.cltr import PyFileChanges


@dataclass(frozen=True, slots=True)
class PureLibTranspiler:
    _python_dir: Path
    _cpp_dir: Path
    _site_packages_dir: Path
    _py_files: list[Path]

    def transpile(self, changes: PyFileChanges, files_deleted: int):
        if len(changes.new_files) > 0 or len(changes.changed_files) > 0:
            bridge_libs = find_bridge_libs(self._site_packages_dir)
            bridge_json_path_cltr = BridgeJsonPathCltr(self._site_packages_dir)
            verify_all_bridge_libs(bridge_libs, bridge_json_path_cltr)
            transpiler = create_transpiler(
                bridge_json_path_cltr, bridge_libs, self._py_files
            )
            transpiler.transpile_all_changed_files(
                changes.new_files,
                changes.changed_files,
                self._python_dir,
                self._cpp_dir,
            )
            r = transpiler.get_results()
            print_transpilation_results(r, files_deleted)
            return r.files_added_or_modified
        return []
