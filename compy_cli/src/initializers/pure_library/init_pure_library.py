import json
from pathlib import Path
import subprocess
from compy_cli.src.dirs_cltr import CompyDirsCltr
from compy_cli.src.lib_dir_cltr import PureLibDirCltr
from compy_cli.src.initializers.util.init_libs import (
    InitLibsHelper,
    create_python_hello_world,
)


def compy_init_pure_library(library_name: str, dirs_cltr: CompyDirsCltr):
    print("creating pure-library files...")
    lib_py_executable: Path = dirs_cltr.calc_lib_py_executable()
    init_libs_helper = InitLibsHelper(
        dirs_cltr.target_dir, lib_py_executable, library_name
    )
    init_libs_helper.create_readme()
    library_name_underscores = library_name.replace("-", "_")
    pure_lib_dir_cltr = PureLibDirCltr(dirs_cltr.target_dir)
    cp: str = "compy-python==0.0.5"
    init_libs_helper.create_pyproject_toml(library_name_underscores, [cp])
    lib_dir: Path = pure_lib_dir_cltr.calc_python_dir(library_name_underscores)
    lib_dir.mkdir()
    cpp_dir: Path = pure_lib_dir_cltr.calc_cpp_dir(library_name_underscores)
    cpp_dir.mkdir()
    compy_data_dir: Path = pure_lib_dir_cltr.calc_compy_data_dir()
    compy_data_dir.mkdir()
    proj_info_file: Path = pure_lib_dir_cltr.calc_proj_info()
    with open(proj_info_file, "w") as f:
        json.dump({"lib_dir_name": library_name_underscores}, f, indent=4)
    create_python_hello_world(lib_dir)
    init_libs_helper.create_python_venv_and_install_hatchling()
    print(f"running 'pip install {cp}'...")
    subprocess.check_call([lib_py_executable, "-m", "pip", "install", cp])
