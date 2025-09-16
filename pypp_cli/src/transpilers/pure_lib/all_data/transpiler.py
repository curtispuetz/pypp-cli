from dataclasses import dataclass
from pathlib import Path

from pypp_cli.src.transpilers.library.bridge_libs.path_cltr import (
    BridgeJsonPathCltr,
)
from pypp_cli.src.transpilers.library.file_changes.cltr import PyFileChanges
from pypp_cli.src.transpilers.library.file_tracker import PyFilesTracker
from pypp_cli.src.transpilers.library.transpiler.transpiler import (
    transpile_all_changed_files,
)


@dataclass(frozen=True, slots=True)
class PureLibTranspiler:
    _python_dir: Path
    _cpp_dir: Path
    _py_files: list[Path]
    _bridge_json_path_cltr: BridgeJsonPathCltr
    _bridge_libs: list[str]

    def transpile(self, changes: PyFileChanges, files_deleted: int):
        if len(changes.new_files) > 0 or len(changes.changed_files) > 0:
            # TODO: fix this.
            results = transpile_all_changed_files(
                self._bridge_json_path_cltr,
                self._bridge_libs,
                self._py_files,
                PyFilesTracker([], set()),
                self._python_dir,
                self._cpp_dir,
                changes.new_files,
                changes.changed_files,
            )
            results.print(files_deleted)
            return results.files_added_or_modified
        return []
