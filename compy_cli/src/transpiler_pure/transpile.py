from dataclasses import dataclass
import json
from pathlib import Path
from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.package_manager.installer.json_validations.util.validations import (
    validate_is_list_of_strings,
)
from compy_cli.src.transpiler.maps.calc_import_map import ImportMap
from compy_cli.src.transpiler.maps.maps import Maps
from compy_cli.src.transpiler.print_results import print_transpilation_results
from compy_cli.src.transpiler.util.deleter import delete_cpp_and_h_files
from compy_cli.src.transpiler.util.file_changes.file_loader import calc_all_py_files
from compy_cli.src.transpiler.util.transpiler import Transpiler, TranspilerDeps
from compy_cli.src.transpiler_pure.file_change_cltr import (
    PureFileChangeCltr,
    PureFileChangeCltrDeps,
)


@dataclass(frozen=True, slots=True)
class PureProjInfo:
    lib_dir_name: str
    ignored_files: list[str]


def load_pure_proj_info(dirs: CompyDirs) -> PureProjInfo:
    with open(dirs.calc_pure_lib_proj_info(), "r") as f:
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


def compy_transpile_pure(dirs: CompyDirs) -> list[Path]:
    proj_info = load_pure_proj_info(dirs)
    py_files: list[Path] = calc_all_py_files(
        dirs.calc_pure_lib_dir(proj_info.lib_dir_name)
    )
    prev_timestamps: dict[str, float] = load_pure_previous_timestamps(
        dirs.calc_pure_lib_timestamps_file()
    )
    pure_file_change_cltr_deps = PureFileChangeCltrDeps(
        dirs.calc_pure_lib_dir(proj_info.lib_dir_name),
        proj_info.ignored_files,
        py_files,
        prev_timestamps,
    )
    pure_file_change_cltr = PureFileChangeCltr(pure_file_change_cltr_deps)
    changes = pure_file_change_cltr.calc_changes()

    files_deleted: int = delete_cpp_and_h_files(
        [changes.deleted_files, changes.changed_files],
        dirs.calc_pure_lib_cpp_dir(proj_info.lib_dir_name),
    )

    cpp_dir = dirs.calc_pure_lib_cpp_dir(proj_info.lib_dir_name)
    python_dir = dirs.calc_pure_lib_dir(proj_info.lib_dir_name)
    transpiler = Transpiler(
        TranspilerDeps(
            # TODO: The first two args dont matter. I will fix that later.
            cpp_dir,
            python_dir,
            cpp_dir,
            python_dir,
            py_files,
            Maps({}, {}, {}, {}, {}, ImportMap(set(), {}), {}),
        )
    )
    transpiler.transpile_all_changed_files(changes.new_files, changes.changed_files)
    r = transpiler.get_results()
    print_transpilation_results(r, files_deleted)
    return r.files_added_or_modified
