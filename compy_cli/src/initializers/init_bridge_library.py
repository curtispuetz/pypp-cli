import json
from pathlib import Path
from compy_cli.src.dirs_cltr import CompyDirsCltr
from compy_cli.src.initializers.util.init_libs import (
    InitLibsHelper,
    create_python_hello_world,
)


def compy_init_bridge_library(library_name: str, dirs_cltr: CompyDirsCltr):
    print("creating bridge-library files...")
    init_libs_helper = InitLibsHelper(
        dirs_cltr.target_dir, dirs_cltr.calc_lib_py_executable(), library_name
    )
    init_libs_helper.create_readme()
    library_name_with_underscores = library_name.replace("-", "_")
    init_libs_helper.create_pyproject_toml(library_name_with_underscores)
    proj_dir: Path = dirs_cltr.target_dir / library_name_with_underscores
    proj_dir.mkdir()
    create_python_hello_world(proj_dir)
    _create_cpp_hello_world(proj_dir)
    _create_import_map(proj_dir)
    init_libs_helper.create_python_venv_and_install_hatchling()


def _create_cpp_hello_world(proj_dir: Path):
    cpp_dir: Path = proj_dir / "compy_data" / "cpp"
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
    bridge_jsons_dir: Path = proj_dir / "compy_data" / "bridge_jsons"
    bridge_jsons_dir.mkdir(parents=True)
    import_map: Path = bridge_jsons_dir / "import_map.json"
    data = {"ignore": []}
    with open(import_map, "w") as f:
        json.dump(data, f, indent=4)
