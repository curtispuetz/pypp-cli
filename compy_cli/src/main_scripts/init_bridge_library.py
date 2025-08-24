import json
from pathlib import Path
import subprocess
import venv
from compy_cli.src.compy_dirs import CompyDirs


def compy_init_bridge_library(library_name: str, dirs: CompyDirs):
    print("creating bridge-library files...")
    _create_readme(dirs, library_name)
    library_name_underscores = library_name.replace("-", "_")
    _create_pyproject_toml(dirs, library_name, library_name_underscores)
    proj_dir: Path = dirs.target_dir / library_name_underscores
    proj_dir.mkdir()
    _create_python_hello_world(proj_dir)
    _create_cpp_hello_world(proj_dir)
    _create_import_map(proj_dir)
    _create_python_venv_and_install_build_requirements(dirs)


def _create_readme(dirs: CompyDirs, library_name: str):
    readme: Path = dirs.target_dir / "readme.md"
    readme.write_text(f"# {library_name}\n")


def _create_pyproject_toml(
    dirs: CompyDirs, library_name: str, library_name_underscores: str
):
    pyproject: Path = dirs.target_dir / "pyproject.toml"
    pyproject.write_text(
        "\n".join(
            [
                "[project]",
                f'name = "{library_name}"',
                'version = "0.0.0"',
                'description = ""',
                "authors = []",
                'readme = "readme.md"',
                'license = {text = "MIT"}',
                "",
                "[tool.setuptools.package-data]",
                f'"{library_name_underscores}" = ["data/**/*"]',
                "",
                "[build-system]",
                'requires = ["setuptools>=61.0"]',
                'build-backend = "setuptools.build_meta"',
            ]
        )
    )


def _create_python_hello_world(proj_dir: Path):
    hello_world: Path = proj_dir / "hello_world.py"
    hello_world.write_text(
        "\n".join(
            [
                "def hello_world_fn() -> str:",
                '    return "Hello, World!"',
            ]
        )
    )


def _create_cpp_hello_world(proj_dir: Path):
    cpp_dir: Path = proj_dir / "data" / "cpp"
    cpp_dir.mkdir(parents=True)
    hello_world_h: Path = cpp_dir / "hello_world.h"
    hello_world_h.write_text(
        "\n".join(
            [
                "#pragma once",
                "",
                "#include <string>",
                "",
                "std::string hello_world_fn();",
            ]
        )
    )
    hello_world_cpp: Path = cpp_dir / "hello_world.cpp"
    hello_world_cpp.write_text(
        "\n".join(
            [
                '#include "hello_world.h"',
                "",
                "std::string hello_world_fn() {",
                '    return "Hello, World!";',
                "}",
            ]
        )
    )


def _create_import_map(proj_dir: Path):
    bridge_jsons_dir: Path = proj_dir / "data" / "bridge_jsons"
    bridge_jsons_dir.mkdir(parents=True)
    import_map: Path = bridge_jsons_dir / "import_map.json"
    data = {"ignore": []}
    with open(import_map, "w") as f:
        json.dump(data, f, indent=4)


def _create_python_venv_and_install_build_requirements(dirs: CompyDirs):
    venv_dir: Path = dirs.target_dir / ".venv"
    print("creating python virtual environment...")
    venv.create(venv_dir, with_pip=True)
    print("python virtual environment created")
    print("installing 'build' library...")
    subprocess.check_call(
        [dirs.calc_bridge_lib_py_executable(), "-m", "pip", "install", "build"]
    )
