import json
from pathlib import Path
import subprocess
from pypp_cli.src.initializers.util.init_libs import (
    InitLibsHelper,
    create_python_hello_world,
)
from pypp_cli.src.other.pypp_paths.init_pure_library import (
    create_init_pure_lib_pypp_paths,
)


def pypp_init_pure_lib(library_name: str, target_dir: Path):
    print("creating pure-library files...")
    python_dir_name = library_name.replace("-", "_")
    paths = create_init_pure_lib_pypp_paths(target_dir, python_dir_name)
    init_libs_helper = InitLibsHelper(target_dir, paths.lib_py_executable, library_name)
    init_libs_helper.create_readme()
    cp: str = "pypp-python"
    init_libs_helper.create_pyproject_toml(python_dir_name, [cp])
    paths.python_dir.mkdir()
    paths.cpp_dir.mkdir()
    paths.pypp_files_dir.mkdir()
    with open(paths.proj_info_file, "w") as f:
        json.dump({"lib_dir_name": python_dir_name}, f, indent=4)
    create_python_hello_world(paths.python_dir)
    init_libs_helper.create_python_venv_and_install_hatchling()
    print(f"running 'pip install {cp}'...")
    subprocess.check_call([paths.lib_py_executable, "-m", "pip", "install", cp])
