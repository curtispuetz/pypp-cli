from pathlib import Path

from pypp_cli.src.transpilers.proj.all_data.create import (
    AllData,
    create_all_data,
)
from pypp_cli.src.other.pypp_paths.do import DoPyppPaths


def pypp_transpile(paths: DoPyppPaths) -> list[Path]:
    a: AllData = create_all_data(paths)

    a.cpp_project_initializer.initialize_if_cpp_dir_is_dirty()

    changes = a.file_change_cltr.calc_changes()

    a.py_files_tracker.handle_deleted_files(changes.deleted_files)

    files_deleted: int = a.cpp_and_h_file_deleter.delete_files(
        [
            changes.deleted_files,
            changes.changed_files,
        ]
    )

    ret = a.main_and_src_transpiler.transpile(changes, files_deleted)

    a.cmake_lists_writer.write()

    a.timestamps_saver.save(changes.new_timestamps)

    return ret
