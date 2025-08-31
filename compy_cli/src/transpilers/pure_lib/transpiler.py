from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.transpilers.other.other.bridge_json_path_cltr import (
    BridgeJsonPathCltr,
)
from compy_cli.src.transpilers.other.other.transpiler.create import (
    create_transpiler,
)
from compy_cli.src.transpilers.other.other.print_results import (
    print_transpilation_results,
)
from compy_cli.src.transpilers.other.other.file_changes.cltr import PyFileChanges


@dataclass(frozen=True, slots=True)
class PureLibTranspiler:
    _python_dir: Path
    _cpp_dir: Path
    _py_files: list[Path]
    _bridge_json_path_cltr: BridgeJsonPathCltr
    _bridge_libs: list[str]

    def transpile(self, changes: PyFileChanges, files_deleted: int):
        if len(changes.new_files) > 0 or len(changes.changed_files) > 0:
            transpiler = create_transpiler(
                self._bridge_json_path_cltr, self._bridge_libs, self._py_files
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
