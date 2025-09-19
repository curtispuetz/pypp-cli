from dataclasses import dataclass
from pathlib import Path

from pypp_cli.do.transpile.calc_file_changes.z.cltr import PyFileChanges
from pypp_cli.do.transpile.find_libs.z.find_all_libs import PyppLibsData
from pypp_cli.do.transpile.z_i.bridge_json_models import (
    BridgeJsonModelsDict,
)
from pypp_cli.do.transpile.z_i.py_file_tracker import PyFilesTracker
from pypp_cli.do.transpile.transpile.z.transpile_all import (
    transpile_all_changed_files,
)


@dataclass(frozen=True, slots=True)
class MainAndSrcTranspiler:
    _namespace: str
    _cpp_dir: Path
    _python_dir: Path
    _libs_data: PyppLibsData
    _py_files: list[Path]
    _bridge_json_models: BridgeJsonModelsDict
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
                self._bridge_json_models,
                self._libs_data,
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
