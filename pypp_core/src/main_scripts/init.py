import json

from pypp_core.src.config import PyppDirs
import os
import venv


def pypp_init(dirs: PyppDirs):
    _create_project_structure(dirs)
    print("py++ project structure creation finished")
    print("creating python virtual environment...")
    _create_python_virtual_environment(dirs)
    print("py++ project init finished")


def _create_python_virtual_environment(dirs: PyppDirs):
    venv_dir = os.path.join(dirs.python_dir, ".venv")
    venv.create(venv_dir, with_pip=True)
    print("Python virtual environment created at:", dirs.python_dir)


def _create_project_structure(dirs: PyppDirs):
    _create_main_folders(dirs)
    _create_python_main_file(dirs)
    _create_python_src_file(dirs)
    _create_proj_json_file(dirs)


def _create_main_folders(dirs: PyppDirs):
    os.makedirs(dirs.cpp_dir, exist_ok=True)
    os.makedirs(dirs.python_dir, exist_ok=True)
    os.makedirs(dirs.python_src_dir, exist_ok=True)
    os.makedirs(dirs.resources_dir, exist_ok=True)
    os.makedirs(dirs.pypp_data_dir, exist_ok=True)


def _create_python_main_file(dirs: PyppDirs):
    main_py_path = os.path.join(dirs.python_dir, "main.py")
    with open(main_py_path, "w") as f:
        f.writelines(
            [
                "from hello_world import first_fn\n",
                "\n",
                "if __name__ == '__main__':\n",
                "    first_fn()\n",
            ]
        )


def _create_python_src_file(dirs: PyppDirs):
    src_py_path = os.path.join(dirs.python_src_dir, "hello_world.py")
    with open(src_py_path, "w") as f:
        f.writelines(["def first_fn():\n", "    print('Hello, World!')\n"])


def _create_proj_json_file(dirs: PyppDirs):
    data: dict = {"cpp_dir_is_dirty": True}
    with open(dirs.proj_info_file, "w") as file:
        json.dump(data, file, indent=4)
