import json
from pathlib import Path
import subprocess

from pypp_core.src.pypp_dirs import PyppDirs
import venv


def pypp_init(dirs: PyppDirs):
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
            r"C:\Users\puetz\PycharmProjects\pypp-python\dist\pypp_python-0.0.0-py3-none-any.whl",
        ]
    )
    print("py++ project init finished")


def _create_python_virtual_environment(dirs: PyppDirs):
    venv_dir: Path = dirs.python_dir / ".venv"
    venv.create(venv_dir, with_pip=True)
    print("Python virtual environment created in python project directory")


def _create_project_structure(dirs: PyppDirs):
    _create_main_folders(dirs)
    _create_python_main_file(dirs)
    _create_python_src_file(dirs)
    _create_proj_json_file(dirs)


def _create_main_folders(dirs: PyppDirs):
    dirs.cpp_dir.mkdir(parents=True, exist_ok=True)
    dirs.python_dir.mkdir(parents=True, exist_ok=True)
    dirs.python_src_dir.mkdir(parents=True, exist_ok=True)
    dirs.resources_dir.mkdir(parents=True, exist_ok=True)
    dirs.pypp_data_dir.mkdir(parents=True, exist_ok=True)


def _create_python_main_file(dirs: PyppDirs):
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


def _create_python_src_file(dirs: PyppDirs):
    src_py_path = dirs.python_src_dir / "hello_world.py"
    src_py_path.write_text(
        "\n".join(
            [
                "def first_fn():",
                "    print('Hello, World!')",
            ]
        )
    )


def _create_proj_json_file(dirs: PyppDirs):
    data = {"cpp_dir_is_dirty": True}
    with open(dirs.proj_info_file, "w") as file:
        json.dump(data, file, indent=4)
