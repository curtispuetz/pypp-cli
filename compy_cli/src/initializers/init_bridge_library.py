import json
from pathlib import Path
from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.initializers.util.init_libs import (
    create_pyproject_toml,
    create_python_hello_world,
    create_python_venv_and_install_hatchling,
    create_readme,
)


def compy_init_bridge_library(library_name: str, dirs: CompyDirs):
    print("creating bridge-library files...")
    create_readme(dirs, library_name)
    library_name_underscores = library_name.replace("-", "_")
    create_pyproject_toml(dirs, library_name, library_name_underscores)
    proj_dir: Path = dirs.target_dir / library_name_underscores
    proj_dir.mkdir()
    create_python_hello_world(proj_dir)
    _create_cpp_hello_world(proj_dir)
    _create_import_map(proj_dir)
    create_python_venv_and_install_hatchling(dirs)


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
