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
    # Create main folders
    os.makedirs(dirs.cpp_dir, exist_ok=True)
    os.makedirs(dirs.python_dir, exist_ok=True)
    os.makedirs(dirs.resources_dir, exist_ok=True)

    # Create python/main.py
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

    # Create python/src directory and hello_world.py
    os.makedirs(dirs.python_src_dir, exist_ok=True)
    src_py_path = os.path.join(dirs.python_src_dir, "hello_world.py")
    with open(src_py_path, "w") as f:
        f.writelines(["def first_fn():\n", "    print('Hello, World!')\n"])
