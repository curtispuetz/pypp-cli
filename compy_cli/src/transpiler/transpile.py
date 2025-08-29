from pathlib import Path

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.transpiler.create_all_data import (
    AllData,
    create_all_data,
)
from compy_cli.src.transpiler.util.transpiler import TranspileResults, Transpiler
from compy_cli.src.transpiler.util.file_changes.file_loader import (
    save_timestamps,
)
from compy_cli.src.transpiler.util.file_changes.calculator import (
    PyFileChanges,
)
from compy_cli.src.transpiler.util.file_changes.file_loader import (
    TimeStampsFile,
)


def compy_transpile(dirs: CompyDirs) -> list[Path]:
    a: AllData = create_all_data(dirs)
    # Step 1: Copy the C++ template to the cpp project directory if marked as dirty
    if a.proj_info.cpp_dir_is_dirty:
        a.cpp_project_initializer.initialize()
    else:
        print("C++ template already copied to the cpp project directory")

    # Step 2: calculate the files that have changed since the last transpile
    src_changes, main_changes = a.file_change_cltr.calc_changes()

    # Step 2.1 write the CMakeLists.txt file
    a.cmake_lists_writer.write(main_changes.ignored_file_stems)

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
    ret = _transpile(a.transpiler, src_changes, main_changes, files_deleted)

    # Step 5: save the file timestamps
    save_timestamps(
        TimeStampsFile(main_changes.new_timestamps, src_changes.new_timestamps),
        dirs.timestamps_file,
    )

    return ret


def _transpile(
    t: Transpiler,
    src_changes: PyFileChanges,
    main_changes: PyFileChanges,
    files_deleted: int,
) -> list[Path]:
    src: TranspileResults = t.transpile_all_changed_files(
        src_changes.new_files, src_changes.changed_files
    )
    main: TranspileResults = t.transpile_all_changed_files(
        main_changes.new_files, main_changes.changed_files, is_main_files=True
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
