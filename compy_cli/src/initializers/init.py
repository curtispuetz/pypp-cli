from dataclasses import dataclass
import json
from pathlib import Path
import subprocess

import venv

from compy_cli.src.dirs_cltr import CompyDirsCltr


def compy_init(dirs_cltr: CompyDirsCltr):
    compy_init_helper = _CompyInitHelper(
        _CompyInitHelperDeps(
            dirs_cltr.calc_python_dir(),
            dirs_cltr.calc_cpp_dir(),
            dirs_cltr.calc_python_src_dir(),
            dirs_cltr.calc_resources_dir(),
            dirs_cltr.calc_compy_data_dir(),
            dirs_cltr.calc_proj_info_file(),
            dirs_cltr.calc_py_executable(),
        )
    )
    compy_init_helper.create_project_structure()
    print("Compy project structure creation finished")
    print("creating python virtual environment...")
    compy_init_helper.create_python_virtual_environment()
    compy_init_helper.install_compy_python()
    print("Compy project init finished")


@dataclass(frozen=True, slots=True)
class _CompyInitHelperDeps:
    python_dir: Path
    cpp_dir: Path
    python_src_dir: Path
    resources_dir: Path
    compy_data_dir: Path
    proj_info_file: Path
    py_executable: Path


class _CompyInitHelper:
    def __init__(self, d: _CompyInitHelperDeps) -> None:
        self._d = d

    def create_python_virtual_environment(self):
        venv_dir: Path = self._d.python_dir / ".venv"
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
        self._d.cpp_dir.mkdir(parents=True, exist_ok=True)
        self._d.python_dir.mkdir(parents=True, exist_ok=True)
        self._d.python_src_dir.mkdir(parents=True, exist_ok=True)
        self._d.resources_dir.mkdir(parents=True, exist_ok=True)
        self._d.compy_data_dir.mkdir(parents=True, exist_ok=True)

    def _create_python_main_file(self):
        main_py_path = self._d.python_dir / "main.py"
        main_py_path.write_text(
            "\n".join(
                [
                    "from hello_world import first_fn",
                    "",
                    "if __name__ == '__main__':",
                    "    first_fn()",
                ]
            )
        )

    def _create_python_src_file(self):
        src_py_path = self._d.python_src_dir / "hello_world.py"
        src_py_path.write_text(
            "\n".join(
                [
                    "def first_fn():",
                    "    print('Hello, World!')",
                ]
            )
        )

    def _create_proj_json_file(self):
        data = {"cpp_dir_is_dirty": True}
        with open(self._d.proj_info_file, "w") as file:
            json.dump(data, file, indent=4)

    def install_compy_python(self):
        subprocess.check_call(
            [
                self._d.py_executable,
                "-m",
                "pip",
                "install",
                # TODO: install from PyPI when available
                r"C:\Users\puetz\PycharmProjects\compy-python\dist"
                r"\compy_python-0.0.0-py3-none-any.whl",
            ]
        )
