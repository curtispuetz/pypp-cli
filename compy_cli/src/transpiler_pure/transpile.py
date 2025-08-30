from dataclasses import dataclass
import json
from pathlib import Path
from compy_cli.src.dirs_cltr import CompyDirsCltr
from compy_cli.src.initializers.pure_library.lib_dir_cltr import (
    PureLibDirCltr,
    PureLibDirCltrDeps,
)
from compy_cli.src.package_manager.installer.json_validations.util.validations import (
    validate_is_list_of_strings,
)
from compy_cli.src.transpiler.maps.util.calc_import_map import ImportMap
from compy_cli.src.transpiler.maps.maps import Maps
from compy_cli.src.transpiler.print_results import print_transpilation_results
from compy_cli.src.transpiler.util.deleter import CppAndHFileDeleter
from compy_cli.src.transpiler.util.file_changes.file_loader import calc_all_py_files
from compy_cli.src.transpiler.util.transpiler._helper import TranspilerDeps
from compy_cli.src.transpiler.util.transpiler.transpiler import (
    Transpiler,
)
from compy_cli.src.transpiler_pure.file_change_cltr import (
    PureFileChangeCltr,
    PureFileChangeCltrDeps,
)


@dataclass(frozen=True, slots=True)
class PureProjInfo:
    lib_dir_name: str
    ignored_files: list[str]


def load_pure_proj_info(proj_info_file: Path) -> PureProjInfo:
    with open(proj_info_file, "r") as f:
        data = json.load(f)
    _validate_pure_proj_info(data)
    return PureProjInfo(data["lib_dir_name"], data.get("ignore_files", []))


def _validate_pure_proj_info(proj_info: object):
    assert isinstance(proj_info, dict), "proj_info.json must be a JSON Object"
    assert "lib_dir_name" in proj_info, "lib_dir_name key missing in proj_info.json"
    assert isinstance(proj_info["lib_dir_name"], str), (
        "lib_dir_name must be a string in proj_info.json"
    )
    if "ignore_files" in proj_info:
        validate_is_list_of_strings(
            ["ignore_files"], proj_info["ignore_files"], "proj_info"
        )


def load_pure_previous_timestamps(timestamps_file: Path) -> dict[str, float]:
    if timestamps_file.exists():
        with open(timestamps_file, "r") as f:
            data = json.load(f)
        return data
    return {}


def compy_transpile_pure(dirs_cltr: CompyDirsCltr) -> list[Path]:
    pure_lib_dir_cltr = PureLibDirCltr(PureLibDirCltrDeps(dirs_cltr.target_dir))
    proj_info = load_pure_proj_info(pure_lib_dir_cltr.calc_pure_lib_proj_info())
    pure_lib_dir = pure_lib_dir_cltr.calc_pure_lib_dir(proj_info.lib_dir_name)
    pure_lib_cpp_dir = pure_lib_dir_cltr.calc_pure_lib_cpp_dir(proj_info.lib_dir_name)
    py_files: list[Path] = calc_all_py_files(pure_lib_dir)
    prev_timestamps: dict[str, float] = load_pure_previous_timestamps(
        pure_lib_dir_cltr.calc_pure_lib_timestamps_file()
    )
    pure_file_change_cltr_deps = PureFileChangeCltrDeps(
        pure_lib_dir,
        proj_info.ignored_files,
        py_files,
        prev_timestamps,
    )
    pure_file_change_cltr = PureFileChangeCltr(pure_file_change_cltr_deps)
    changes = pure_file_change_cltr.calc_changes()

    cpp_and_h_file_deleter = CppAndHFileDeleter(pure_lib_cpp_dir)
    files_deleted: int = cpp_and_h_file_deleter.delete_files(
        [changes.deleted_files, changes.changed_files]
    )

    transpiler = Transpiler(
        TranspilerDeps(
            py_files,
            Maps({}, {}, {}, {}, {}, ImportMap(set(), {}), {}),
        )
    )
    transpiler.transpile_all_changed_files(
        changes.new_files, changes.changed_files, pure_lib_dir, pure_lib_cpp_dir
    )
    r = transpiler.get_results()
    print_transpilation_results(r, files_deleted)
    return r.files_added_or_modified
