import json
from pathlib import Path
import subprocess

from compy_cli.src.compy_dirs import CompyDirs
import venv

# TODO: rename project to compy


def pypp_init(dirs: CompyDirs):
    _create_project_structure(dirs)
    print("py++ project structure creation finished")
    print("creating python virtual environment...")
    _create_python_virtual_environment(dirs)
    subprocess.check_call(
        [
            dirs.calc_py_executable(),
            "-m",
            "pip",
            "install",
            # TODO later: install from PyPI when available
            # TODO now: update path
            r"C:\Users\puetz\PycharmProjects\compy-python\dist\compy_python-0.0.0-py3-none-any.whl",
        ]
    )
    print("py++ project init finished")


def _create_python_virtual_environment(dirs: CompyDirs):
    venv_dir: Path = dirs.python_dir / ".venv"
    venv.create(venv_dir, with_pip=True)
    print("Python virtual environment created in python project directory")


def _create_project_structure(dirs: CompyDirs):
    _create_main_folders(dirs)
    _create_python_main_file(dirs)
    _create_python_src_file(dirs)
    _create_proj_json_file(dirs)


def _create_main_folders(dirs: CompyDirs):
    dirs.cpp_dir.mkdir(parents=True, exist_ok=True)
    dirs.python_dir.mkdir(parents=True, exist_ok=True)
    dirs.python_src_dir.mkdir(parents=True, exist_ok=True)
    dirs.resources_dir.mkdir(parents=True, exist_ok=True)
    dirs.compy_data_dir.mkdir(parents=True, exist_ok=True)


def _create_python_main_file(dirs: CompyDirs):
    main_py_path = dirs.python_dir / "main.py"
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


def _create_python_src_file(dirs: CompyDirs):
    src_py_path = dirs.python_src_dir / "hello_world.py"
    src_py_path.write_text(
        "\n".join(
            [
                "def first_fn():",
                "    print('Hello, World!')",
            ]
        )
    )


def _create_proj_json_file(dirs: CompyDirs):
    data = {"cpp_dir_is_dirty": True}
    with open(dirs.proj_info_file, "w") as file:
        json.dump(data, file, indent=4)
