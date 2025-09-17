from dataclasses import dataclass
from pathlib import Path

from pypp_cli.src.transpilers.library.bridge_libs.finder import PyppLibs
from pypp_cli.src.transpilers.library.bridge_libs.path_cltr import (
    BridgeJsonPathCltr,
)
from pypp_cli.src.transpilers.library.file_tracker import PyFilesTracker
from pypp_cli.src.transpilers.library.file_changes.cltr import PyFileChanges
from pypp_cli.src.transpilers.library.transpiler.transpiler import (
    transpile_all_changed_files,
)


@dataclass(frozen=True, slots=True)
class MainAndSrcTranspiler:
    _namespace: str | None
    _cpp_dir: Path
    _python_dir: Path
    _libs: PyppLibs
    _py_files: list[Path]
    _bridge_json_path_cltr: BridgeJsonPathCltr
    _py_files_tracker: PyFilesTracker

    def transpile(
        self,
        changes: PyFileChanges,
        files_deleted: int,
    ) -> list[Path]:
        self._cpp_dir.mkdir(parents=True, exist_ok=True)
        if len(changes.new_files) > 0 or len(changes.changed_files) > 0:
            results = transpile_all_changed_files(
                self._namespace,
                self._bridge_json_path_cltr,
                self._libs,
                self._py_files,
                self._py_files_tracker,
                self._python_dir,
                self._cpp_dir,
                changes.new_files,
                changes.changed_files,
            )
            results.print(files_deleted)
            return results.files_added_or_modified
        return []
