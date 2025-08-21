import ast
import json
from pathlib import Path

from pypp_core.src.config import PyppDirs, create_test_dir_pypp_dirs
from pypp_core.src.constants import SECRET_MAIN_FILE_DIR_PREFIX
from pypp_core.src.mapping.maps.maps import Maps, calc_maps
from pypp_core.src.util.file_change_tracker import (
    calc_py_file_changes,
    get_all_main_py_files,
    save_timestamps,
)
from pypp_core.src.util.initalize_cpp import (
    initialize_cpp_project,
)
from pypp_core.src.util.calc_ast_tree import (
    calc_ast_tree,
)
from pypp_core.src.util.main_source import (
    calc_main_cpp_source,
    calc_src_file_cpp_and_h_source,
)
from pypp_core.src.util.write_cmake_lists import write_cmake_lists_file


def _delete_cpp_and_h_file(filepath: Path, dirs: PyppDirs) -> int:
    files_deleted: int = 0
    cpp_file: Path = filepath.with_suffix(".cpp")
    h_file: Path = filepath.with_suffix(".h")
    cpp_full_path: Path = dirs.cpp_src_dir / cpp_file
    h_full_path: Path = dirs.cpp_src_dir / h_file
    if cpp_full_path.exists():
        cpp_full_path.unlink()
        files_deleted += 1
    if h_full_path.exists():
        h_full_path.unlink()
        files_deleted += 1
    return files_deleted


def _transpile_cpp_and_h_files(
    rel_path: Path,
    files_added_or_modified: list[Path],
    dirs: PyppDirs,
    header_files_written: int,
    cpp_files_written: int,
    proj_info: dict,
    maps: Maps,
) -> tuple[int, int]:
    if rel_path.name.startswith(SECRET_MAIN_FILE_DIR_PREFIX):
        # transpile a main file
        real_rel_path = rel_path.with_name(
            rel_path.name[len(SECRET_MAIN_FILE_DIR_PREFIX) :]
        )
        py_main_file: Path = dirs.python_dir / real_rel_path
        main_py_ast_tree: ast.Module = calc_ast_tree(py_main_file)
        main_cpp_source: str = calc_main_cpp_source(main_py_ast_tree, proj_info, maps)
        new_file_rel: Path = real_rel_path.with_suffix(".cpp")
        new_file: Path = dirs.cpp_dir / new_file_rel
        new_file.write_text(main_cpp_source)
        cpp_files_written += 1
        files_added_or_modified.append(Path(new_file))
    else:
        # transpile src file
        py_src_file: Path = dirs.python_src_dir / rel_path
        src_file_py_ast_tree: ast.Module = calc_ast_tree(py_src_file)
        cpp_file: Path = rel_path.with_suffix(".cpp")
        h_file: Path = rel_path.with_suffix(".h")
        cpp, h = calc_src_file_cpp_and_h_source(
            src_file_py_ast_tree, h_file, proj_info, maps
        )
        cpp_full_path: Path = dirs.cpp_src_dir / cpp_file
        full_dir: Path = cpp_full_path.parent
        full_dir.mkdir(parents=True, exist_ok=True)
        if cpp != "":
            cpp_full_path.write_text(cpp)
            cpp_files_written += 1
            files_added_or_modified.append(cpp_full_path)
        h_full_path: Path = dirs.cpp_src_dir / h_file
        h_full_path.write_text(h)
        header_files_written += 1
        files_added_or_modified.append(h_full_path)
    return header_files_written, cpp_files_written


def pypp_transpile(dirs: PyppDirs) -> list[Path]:
    # Step 1: Copy the C++ template to the cpp project directory if marked as dirty
    with open(dirs.proj_info_file) as file:
        proj_info = json.load(file)
    if proj_info["cpp_dir_is_dirty"]:
        initialize_cpp_project(dirs, proj_info)
    else:
        print("C++ template already copied to the cpp project directory")
    # Step 1.1 write the CmakeLists.txt file
    main_py_files: list[Path] = get_all_main_py_files(dirs.python_dir)
    if not main_py_files:
        raise Exception(f"No Python files (*.py) found in '{dirs.python_dir}'.")
    write_cmake_lists_file(dirs, main_py_files)

    # Step 2: calculate the files that have changed since the last transpile
    py_file_changes, file_timestamps = calc_py_file_changes(
        dirs, proj_info["ignore_src_files"], main_py_files
    )

    # Step 3: iterate over the deleted Py files and delete the corresponding C++ files
    files_deleted: int = 0
    for deleted_file in py_file_changes.deleted_files + py_file_changes.changed_files:
        files_deleted += _delete_cpp_and_h_file(deleted_file, dirs)

    # Step 4: iterate over the changes and now files and transpile them
    assert dirs.python_src_dir.exists(), "src/ dir must be defined; dir not found"
    dirs.cpp_src_dir.mkdir(parents=True, exist_ok=True)
    py_files_transpiled: int = 0
    header_files_written: int = 0
    cpp_files_written: int = 0
    files_added_or_modified: list[Path] = []
    changed_and_new_files: list[Path] = (
        py_file_changes.new_files + py_file_changes.changed_files
    )
    maps: Maps | None = None
    for changed_or_new_file in changed_and_new_files:
        if maps is None:
            maps = calc_maps(proj_info, dirs)
        py_files_transpiled += 1
        print(changed_or_new_file)
        header_files_written, cpp_files_written = _transpile_cpp_and_h_files(
            changed_or_new_file,
            files_added_or_modified,
            dirs,
            header_files_written,
            cpp_files_written,
            proj_info,
            maps,
        )
    print(
        f"py++ transpile finished. "
        f"files deleted: {files_deleted}, "
        f"py files transpiled: {py_files_transpiled}, "
        f"header files written: {header_files_written}, "
        f"cpp files written: {cpp_files_written}"
    )

    # Step 5: save the file timestamps
    save_timestamps(file_timestamps, dirs.timestamps_file)

    return files_added_or_modified


if __name__ == "__main__":
    pypp_transpile(create_test_dir_pypp_dirs())
