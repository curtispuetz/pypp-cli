import json
from pathlib import Path
import subprocess
from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.initializers.util.init_libs import (
    create_pyproject_toml,
    create_python_hello_world,
    create_python_venv_and_install_hatchling,
    create_readme,
)


def compy_init_pure_library(library_name: str, dirs: CompyDirs):
    print("creating pure-library files...")
    create_readme(dirs, library_name)
    library_name_underscores = library_name.replace("-", "_")
    cp: str = "compy-python==0.0.5"
    create_pyproject_toml(dirs, library_name, library_name_underscores, [cp])
    lib_dir: Path = dirs.calc_pure_lib_dir(library_name_underscores)
    lib_dir.mkdir()
    cpp_dir: Path = dirs.calc_pure_lib_cpp_dir(library_name_underscores)
    cpp_dir.mkdir()
    compy_data_dir: Path = dirs.calc_pure_lib_compy_data_dir()
    compy_data_dir.mkdir()
    proj_info_file: Path = dirs.calc_pure_lib_proj_info()
    with open(proj_info_file, "w") as f:
        json.dump({"lib_dir_name": library_name_underscores}, f, indent=4)
    create_python_hello_world(lib_dir)
    create_python_venv_and_install_hatchling(dirs)
    print(f"running 'pip install {cp}'...")
    subprocess.check_call([dirs.calc_lib_py_executable(), "-m", "pip", "install", cp])
