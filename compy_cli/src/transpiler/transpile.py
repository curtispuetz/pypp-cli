from pathlib import Path

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.transpiler.create_all_data import (
    AllData,
    CalcChangesDeps,
    TranspileDeps,
    create_all_data,
)
from compy_cli.src.transpiler.util.calculator import (
    TranspileResults,
    transpile_all_changed_files,
)
from compy_cli.src.transpiler.util.file_changes.calculator import (
    save_timestamps,
)
from compy_cli.src.transpiler.util.file_changes.file_change_tracker_2 import (
    PyFileChanges,
    calc_py_file_changes,
)
from compy_cli.src.transpiler.util.file_changes.calculator import (
    TimeStampsFile,
)
from compy_cli.src.transpiler.util.initalize_cpp import (
    initialize_cpp_project,
)
from compy_cli.src.transpiler.util.write_cmake_lists import write_cmake_lists_file


def compy_transpile(dirs: CompyDirs) -> list[Path]:
    all_data: AllData = create_all_data(dirs)
    # Step 1: Copy the C++ template to the cpp project directory if marked as dirty
    if all_data.proj_info.cpp_dir_is_dirty:
        initialize_cpp_project(all_data.initialize_cpp_project_deps)
    else:
        print("C++ template already copied to the cpp project directory")

    # Step 2: calculate the files that have changed since the last transpile
    src_changes, main_changes = _calc_changes(all_data.calc_changes_deps)

    # Step 2.1 write the CMakeLists.txt file
    write_cmake_lists_file(
        all_data.write_cmake_lists_file_deps,
        main_changes.ignored_file_stems,
    )

    # Step 3: iterate over the deleted Py files and delete the corresponding C++ files
    files_deleted: int = 0
    for files in [
        src_changes.deleted_files,
        main_changes.deleted_files,
        src_changes.changed_files,
        main_changes.changed_files,
    ]:
        for file in files:
            files_deleted += _delete_cpp_and_h_file(file, dirs)

    # Step 4: iterate over the changes and new files and transpile them
    assert dirs.python_src_dir.exists(), "src/ dir must be defined; dir not found"
    dirs.cpp_src_dir.mkdir(parents=True, exist_ok=True)
    ret = _transpile(all_data.transpile_deps, src_changes, main_changes, files_deleted)

    # Step 5: save the file timestamps
    save_timestamps(
        TimeStampsFile(main_changes.new_timestamps, src_changes.new_timestamps),
        dirs.timestamps_file,
    )

    return ret


def _transpile(
    d: TranspileDeps,
    src_changes: PyFileChanges,
    main_changes: PyFileChanges,
    files_deleted: int,
) -> list[Path]:
    src: TranspileResults = transpile_all_changed_files(
        d, src_changes.new_files, src_changes.changed_files
    )
    main: TranspileResults = transpile_all_changed_files(
        d, main_changes.new_files, main_changes.changed_files, is_main_files=True
    )

    print(
        f"Compy transpile finished. "
        f"files deleted: {files_deleted}, "
        f"py files transpiled: "
        f"{src.py_files_transpiled + main.py_files_transpiled}, "
        f"header files written: "
        f"{src.header_files_written + main.header_files_written},"
        f" cpp files written: "
        f"{src.cpp_files_written + main.cpp_files_written}"
    )

    return src.files_added_or_modified + main.files_added_or_modified


def _calc_changes(d: CalcChangesDeps) -> tuple[PyFileChanges, PyFileChanges]:
    src = calc_py_file_changes(
        d.prev_timestamps.src_files,
        d.dirs.python_src_dir,
        d.proj_info.ignored_src_files,
        d.src_py_files,
    )
    main = calc_py_file_changes(
        d.prev_timestamps.main_files,
        d.dirs.python_dir,
        d.proj_info.ignored_main_files,
        d.main_py_files,
    )

    if not (
        src.changed_files
        or src.new_files
        or src.deleted_files
        or main.changed_files
        or main.new_files
        or main.deleted_files
    ):
        print("No file changes detected.")
    else:
        print(
            f"changed files: {len(src.changed_files) + len(main.changed_files)}, "
            f"new files: {len(src.new_files) + len(main.new_files)}, "
            f"deleted files: {len(src.deleted_files) + len(main.deleted_files)},"
            f" ignored files: {
                list(src.ignored_file_stems) + list(main.ignored_file_stems)
            }"
        )

    return src, main


def _delete_cpp_and_h_file(filepath: Path, dirs: CompyDirs) -> int:
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
