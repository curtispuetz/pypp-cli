from dataclasses import dataclass
from pathlib import Path

from pypp_cli.src.transpilers.library.bridge_libs.path_cltr import (
    BridgeJsonPathCltr,
)
from pypp_cli.src.transpilers.library.file_tracker import PyFilesTracker
from pypp_cli.src.transpilers.library.transpiler.create import (
    create_transpiler,
)
from pypp_cli.src.transpilers.library.file_changes.cltr import PyFileChanges


@dataclass(frozen=True, slots=True)
class MainAndSrcTranspiler:
    _cpp_dir: Path
    _python_dir: Path
    _bridge_libs: list[str]
    _src_py_files: list[Path]
    _bridge_json_path_cltr: BridgeJsonPathCltr
    _py_files_tracker: PyFilesTracker

    def transpile(
        self,
        changes: PyFileChanges,
        files_deleted: int,
    ) -> list[Path]:
        self._cpp_dir.mkdir(parents=True, exist_ok=True)
        if len(changes.new_files) > 0 or len(changes.changed_files) > 0:
            t = create_transpiler(
                self._bridge_json_path_cltr,
                self._bridge_libs,
                self._src_py_files,
                self._py_files_tracker,
            )
            t.transpile_all_changed_files(
                changes.new_files,
                changes.changed_files,
                self._python_dir,
                self._cpp_dir,
            )
            r = t.get_results()
            r.print(files_deleted)
            return r.files_added_or_modified
        return []
