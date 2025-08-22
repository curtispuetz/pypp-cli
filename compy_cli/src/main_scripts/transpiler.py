import ast
from pathlib import Path
from pypp_core.src.pypp_dirs import PyppDirs
from pypp_core.src.mapping.maps.maps import Maps, calc_maps
from pypp_core.src.util.calc_ast_tree import calc_ast_tree
from pypp_core.src.util.file_change_tracker import PyChangedFile, PyFileChanges
from pypp_core.src.util.source_calculator import (
    calc_main_cpp_source,
    calc_src_file_cpp_and_h_source,
)


class Transpiler:
    def __init__(
        self, dirs: PyppDirs, proj_info: dict, src_py_files: list[Path]
    ) -> None:
        self._dirs = dirs
        self._proj_info = proj_info
        self._src_py_files = src_py_files
        self.files_added_or_modified: list[Path] = []
        self.py_files_transpiled: int = 0
        self.header_files_written: int = 0
        self.cpp_files_written: int = 0

    def transpile_all_changed_files(self, py_file_changes: PyFileChanges):
        maps: Maps | None = None
        for file in py_file_changes.new_files + py_file_changes.changed_files:
            self.py_files_transpiled += 1
            if maps is None:
                maps = calc_maps(self._proj_info, self._dirs)
            self._transpile_cpp_and_h_files(file, maps)

    def _transpile_cpp_and_h_files(
        self,
        changed_or_new_file: PyChangedFile,
        maps: Maps,
    ):
        if changed_or_new_file.is_main_file:
            py_main_file: Path = self._dirs.python_dir / changed_or_new_file.rel_path
            main_py_ast_tree: ast.Module = calc_ast_tree(py_main_file)
            main_cpp_source: str = calc_main_cpp_source(
                main_py_ast_tree, maps, self._src_py_files
            )
            new_file_rel: Path = changed_or_new_file.rel_path.with_suffix(".cpp")
            new_file: Path = self._dirs.cpp_dir / new_file_rel
            new_file.write_text(main_cpp_source)
            self.cpp_files_written += 1
            self.files_added_or_modified.append(Path(new_file))
        else:  # src file
            py_src_file: Path = self._dirs.python_src_dir / changed_or_new_file.rel_path
            src_file_py_ast_tree: ast.Module = calc_ast_tree(py_src_file)
            cpp_file: Path = changed_or_new_file.rel_path.with_suffix(".cpp")
            h_file: Path = changed_or_new_file.rel_path.with_suffix(".h")
            cpp, h = calc_src_file_cpp_and_h_source(
                src_file_py_ast_tree, h_file, maps, self._src_py_files
            )
            cpp_full_path: Path = self._dirs.cpp_src_dir / cpp_file
            full_dir: Path = cpp_full_path.parent
            full_dir.mkdir(parents=True, exist_ok=True)
            if cpp != "":
                cpp_full_path.write_text(cpp)
                self.cpp_files_written += 1
                self.files_added_or_modified.append(cpp_full_path)
            h_full_path: Path = self._dirs.cpp_src_dir / h_file
            h_full_path.write_text(h)
            self.header_files_written += 1
            self.files_added_or_modified.append(h_full_path)
