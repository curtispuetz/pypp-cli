from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.bridge_json_path_cltr import BridgeJsonPathCltr
from compy_cli.src.transpiler.create_transpler_data import create_transpiler
from compy_cli.src.transpiler.print_results import print_transpilation_results
from compy_cli.src.transpiler.util.file_changes.cltr import PyFileChanges


@dataclass(frozen=True, slots=True)
class MainAndSrcTranspiler:
    _cpp_dir: Path
    _python_dir: Path
    _cpp_src_dir: Path
    _python_src_dir: Path
    _installed_bridge_libs: dict[str, str]
    _src_py_files: list[Path]
    _bridge_json_path_cltr: BridgeJsonPathCltr

    def transpile(
        self,
        src_changes: PyFileChanges,
        main_changes: PyFileChanges,
        files_deleted: int,
    ) -> list[Path]:
        assert self._python_src_dir.exists(), "src/ dir must be defined; dir not found"
        self._cpp_src_dir.mkdir(parents=True, exist_ok=True)
        if (
            len(src_changes.new_files) > 0
            or len(src_changes.changed_files) > 0
            or len(main_changes.new_files) > 0
            or len(main_changes.changed_files) > 0
        ):
            t = create_transpiler(
                self._bridge_json_path_cltr,
                self._installed_bridge_libs,
                self._src_py_files,
            )
            t.transpile_all_changed_files(
                src_changes.new_files,
                src_changes.changed_files,
                self._python_src_dir,
                self._cpp_src_dir,
            )
            t.transpile_all_changed_files(
                main_changes.new_files,
                main_changes.changed_files,
                self._python_dir,
                self._cpp_dir,
                is_main_files=True,
            )
            r = t.get_results()
            print_transpilation_results(r, files_deleted)
            return r.files_added_or_modified
        return []
