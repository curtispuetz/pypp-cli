from pathlib import Path
from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.main_scripts.util.init_libs import (
    create_pyproject_toml,
    create_python_hello_world,
    create_python_venv_and_install_hatchling,
    create_readme,
)
from compy_cli.src.main_scripts.util.pip_helper import pip_install


def compy_init_pure_library(library_name: str, dirs: CompyDirs):
    print("creating pure-library files...")
    create_readme(dirs, library_name)
    library_name_underscores = library_name.replace("-", "_")
    cp: str = "compy-python==0.0.5"
    create_pyproject_toml(dirs, library_name, library_name_underscores, [cp])
    proj_dir: Path = dirs.target_dir / library_name_underscores
    proj_dir.mkdir()
    create_python_hello_world(proj_dir)
    create_python_venv_and_install_hatchling(dirs)
    pip_install(cp, dirs)
