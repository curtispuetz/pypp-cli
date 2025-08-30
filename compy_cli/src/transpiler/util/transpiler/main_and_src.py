from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.bridge_json_path_cltr import BridgeJsonPathCltr
from compy_cli.src.transpiler.create_transpler_data import create_transpiler_data
from compy_cli.src.transpiler.print_results import print_transpilation_results
from compy_cli.src.transpiler.util.file_changes.cltr import PyFileChanges


@dataclass(frozen=True, slots=True)
class MainAndSrcTranspilerDeps:
    cpp_dir: Path
    python_dir: Path
    cpp_src_dir: Path
    python_src_dir: Path
    installed_bridge_libs: dict[str, str]
    src_py_files: list[Path]
    bridge_json_path_cltr: BridgeJsonPathCltr


class MainAndSrcTranspiler:
    def __init__(self, d: MainAndSrcTranspilerDeps) -> None:
        self._d = d

    def transpile(
        self,
        src_changes: PyFileChanges,
        main_changes: PyFileChanges,
        files_deleted: int,
    ) -> list[Path]:
        assert self._d.python_src_dir.exists(), (
            "src/ dir must be defined; dir not found"
        )
        self._d.cpp_src_dir.mkdir(parents=True, exist_ok=True)
        if (
            len(src_changes.new_files) > 0
            or len(src_changes.changed_files) > 0
            or len(main_changes.new_files) > 0
            or len(main_changes.changed_files) > 0
        ):
            a = create_transpiler_data(
                self._d.bridge_json_path_cltr,
                self._d.installed_bridge_libs,
                self._d.src_py_files,
            )
            a.transpiler.transpile_all_changed_files(
                src_changes.new_files,
                src_changes.changed_files,
                self._d.python_src_dir,
                self._d.cpp_src_dir,
            )
            a.transpiler.transpile_all_changed_files(
                main_changes.new_files,
                main_changes.changed_files,
                self._d.python_dir,
                self._d.cpp_dir,
                is_main_files=True,
            )
            r = a.transpiler.get_results()
            print_transpilation_results(r, files_deleted)
            return r.files_added_or_modified
        return []
