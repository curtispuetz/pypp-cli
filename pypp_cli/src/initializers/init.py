from dataclasses import dataclass
import json
from pathlib import Path
import subprocess

import venv

from pypp_cli.src.other.pypp_paths.init import InitPyppPaths, create_init_pypp_paths


def pypp_init(target_dir: Path):
    pypp_init_helper = _PyppInitHelper(create_init_pypp_paths(target_dir))
    pypp_init_helper.create_project_structure()
    print("Py++ project structure creation finished")
    print("creating python virtual environment...")
    pypp_init_helper.create_python_virtual_environment()
    pypp_init_helper.install_pypp_python()
    print("Py++ project init finished")


@dataclass(frozen=True, slots=True)
class _PyppInitHelper:
    _paths: InitPyppPaths

    def create_python_virtual_environment(self):
        venv_dir: Path = self._paths.python_dir / ".venv"
        venv.create(venv_dir, with_pip=True)
        print("Python virtual environment created in python project directory")

    def create_project_structure(
        self,
    ):
        self._create_main_folders()
        self._create_python_main_file()
        self._create_python_src_file()
        self._create_proj_json_file()

    def _create_main_folders(
        self,
    ):
        self._paths.cpp_dir.mkdir(parents=True, exist_ok=True)
        self._paths.python_dir.mkdir(parents=True, exist_ok=True)
        self._paths.python_src_dir.mkdir(parents=True, exist_ok=True)
        self._paths.resources_dir.mkdir(parents=True, exist_ok=True)
        self._paths.pypp_files_dir.mkdir(parents=True, exist_ok=True)

    def _create_python_main_file(self):
        main_py_path = self._paths.python_dir / "main.py"
        main_py_path.write_text(
            "\n".join(
                [
                    "# main file example",
                    "",
                    "from hello_world import first_fn",
                    "",
                    "if __name__ == '__main__':",
                    "    first_fn()",
                ]
            )
        )

    def _create_python_src_file(self):
        src_py_path = self._paths.python_src_dir / "hello_world.py"
        src_py_path.write_text(
            "\n".join(
                [
                    "# src file example",
                    "",
                    "def first_fn():",
                    "    print('Hello, World!')",
                ]
            )
        )

    def _create_proj_json_file(self):
        data = {"cpp_dir_is_dirty": True}
        with open(self._paths.proj_info_file, "w") as file:
            json.dump(data, file, indent=4)

    def install_pypp_python(self):
        subprocess.check_call(
            [
                self._paths.py_executable,
                "-m",
                "pip",
                "install",
                "pypp-python",
            ]
        )
