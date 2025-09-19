from pathlib import Path

from pypp_cli.do.transpile.z.create import (
    AllData,
    create_all_data,
)
from pypp_cli.do.z.paths.do import DoTranspileDeps


def pypp_transpile(transpile_deps: DoTranspileDeps) -> list[Path]:
    a: AllData = create_all_data(transpile_deps)

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

    a.metadata_saver.save_if_required()

    return ret
