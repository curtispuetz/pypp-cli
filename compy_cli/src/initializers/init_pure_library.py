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
    proj_dir: Path = dirs.target_dir / library_name_underscores
    proj_dir.mkdir()
    cpp_dir: Path = proj_dir / "cpp"
    cpp_dir.mkdir()
    compy_data_dir: Path = dirs.target_dir / "compy_data"
    compy_data_dir.mkdir()
    create_python_hello_world(proj_dir)
    create_python_venv_and_install_hatchling(dirs)
    print(f"running 'pip install {cp}'...")
    subprocess.check_call([dirs.calc_lib_py_executable(), "-m", "pip", "install", cp])
