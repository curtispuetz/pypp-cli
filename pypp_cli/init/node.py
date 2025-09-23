from dataclasses import dataclass
import json
from pathlib import Path

from pypp_cli.y.proj_info import ProjInfo
from pypp_cli.init.z.paths.init import InitPyppPaths, create_init_pypp_paths


def pypp_init(target_dir: Path):
    pypp_init_helper = _PyppInitHelper(create_init_pypp_paths(target_dir))
    pypp_init_helper.create_project_structure()
    print("Py++ project init finished")


PROJ_INFO_DEFAULTS = ProjInfo(
    namespace="me",
    override_cpp_write_dir=None,
    write_metadata_to_dir=None,
    ignored_files=[],
    cmake_minimum_required_version="4.0",
    cpp_dir_is_dirty=True,
)


@dataclass(frozen=True, slots=True)
class _PyppInitHelper:
    _paths: InitPyppPaths

    def create_project_structure(
        self,
    ):
        self._create_cpp_and_resources_dirs()
        self._create_python_main_file()
        self._create_proj_json_file()

    def _create_cpp_and_resources_dirs(
        self,
    ):
        self._paths.cpp_dir.mkdir(parents=True, exist_ok=True)
        self._paths.resources_dir.mkdir(parents=True, exist_ok=True)

    def _create_python_main_file(self):
        main_py_path = self._paths.root_dir / "main.py"
        main_py_path.write_text(
            "\n".join(
                [
                    "if __name__ == '__main__':",
                    "    print('Hello from Py++ project!')",
                ]
            )
        )

    def _create_proj_json_file(self):
        with open(self._paths.proj_info_file, "w") as file:
            json.dump(PROJ_INFO_DEFAULTS.model_dump(), file, indent=4)
