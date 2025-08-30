from pathlib import Path

from compy_cli.src.dirs_cltr import CompyDirsCltr
from compy_cli.src.transpiler.create_all_data import (
    AllData,
    create_all_data,
)
from compy_cli.src.transpiler.util.file_changes.file_loader import (
    TimeStampsFile,
)


def compy_transpile(dirs_cltr: CompyDirsCltr) -> list[Path]:
    a: AllData = create_all_data(dirs_cltr)

    a.cpp_project_initializer.initialize_of_cpp_dir_is_dirty()

    src_changes, main_changes = a.file_change_cltr.calc_changes()

    a.cmake_lists_writer.write(main_changes.ignored_file_stems)

    files_deleted: int = a.cpp_and_h_file_deleter.delete_files(
        [
            src_changes.deleted_files,
            main_changes.deleted_files,
            src_changes.changed_files,
            main_changes.changed_files,
        ]
    )

    ret = a.main_and_src_transpiler.transpile(src_changes, main_changes, files_deleted)

    a.timestamps_saver.save(
        TimeStampsFile(main_changes.new_timestamps, src_changes.new_timestamps)
    )

    return ret
