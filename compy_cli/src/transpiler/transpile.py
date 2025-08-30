from pathlib import Path

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.transpiler.create_all_data import (
    AllData,
    create_all_data,
)
from compy_cli.src.transpiler.create_transpler_data import create_transpiler_data
from compy_cli.src.transpiler.print_results import print_transpilation_results
from compy_cli.src.transpiler.util.deleter import delete_cpp_and_h_files
from compy_cli.src.transpiler.util.file_changes.file_loader import (
    save_timestamps,
)
from compy_cli.src.transpiler.util.file_changes.cltr import (
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
    files_deleted: int = delete_cpp_and_h_files(
        [
            src_changes.deleted_files,
            main_changes.deleted_files,
            src_changes.changed_files,
            main_changes.changed_files,
        ],
        dirs.cpp_src_dir,
    )

    # Step 4: iterate over the changes and new files and transpile them
    assert dirs.python_src_dir.exists(), "src/ dir must be defined; dir not found"
    dirs.cpp_src_dir.mkdir(parents=True, exist_ok=True)
    ret = _transpile(
        dirs,
        a.src_py_files,
        a.proj_info.installed_bridge_libs,
        src_changes,
        main_changes,
        files_deleted,
    )

    # Step 5: save the file timestamps
    save_timestamps(
        TimeStampsFile(main_changes.new_timestamps, src_changes.new_timestamps),
        dirs.timestamps_file,
    )

    return ret


def _transpile(
    dirs: CompyDirs,
    src_py_files: list[Path],
    installed_bridge_libs: dict[str, str],
    src_changes: PyFileChanges,
    main_changes: PyFileChanges,
    files_deleted: int,
) -> list[Path]:
    if (
        len(src_changes.new_files) > 0
        or len(src_changes.changed_files) > 0
        or len(main_changes.new_files) > 0
        or len(main_changes.changed_files) > 0
    ):
        a = create_transpiler_data(dirs, installed_bridge_libs, src_py_files)
        a.transpiler.transpile_all_changed_files(
            src_changes.new_files, src_changes.changed_files
        )
        a.transpiler.transpile_all_changed_files(
            main_changes.new_files, main_changes.changed_files, is_main_files=True
        )
        r = a.transpiler.get_results()
        print_transpilation_results(r, files_deleted)
        return r.files_added_or_modified
    return []
