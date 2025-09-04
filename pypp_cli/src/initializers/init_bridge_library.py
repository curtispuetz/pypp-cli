import json
from pathlib import Path
from pypp_cli.src.initializers.util.init_libs import (
    InitLibsHelper,
    create_python_hello_world,
)
from pypp_cli.src.other.pypp_paths.init_bridge_library import (
    create_init_bridge_lib_pypp_paths,
)


def pypp_init_bridge_library(library_name: str, target_dir: Path):
    print("creating bridge-library files...")
    python_dir_name = library_name.replace("-", "_")
    paths = create_init_bridge_lib_pypp_paths(target_dir, python_dir_name)
    init_libs_helper = InitLibsHelper(target_dir, paths.lib_py_executable, library_name)
    init_libs_helper.create_readme()
    init_libs_helper.create_pyproject_toml(python_dir_name)
    paths.python_dir.mkdir()
    create_python_hello_world(paths.python_dir)
    _create_cpp_hello_world(paths.cpp_dir, paths.hello_world_h, paths.hello_world_cpp)
    _create_import_map(paths.bridge_jsons_dir, paths.import_map_json)
    init_libs_helper.create_python_venv_and_install_hatchling()


def _create_cpp_hello_world(cpp_dir: Path, hello_world_h: Path, hello_world_cpp: Path):
    cpp_dir.mkdir(parents=True)
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


def _create_import_map(bridge_jsons_dir: Path, import_map: Path):
    bridge_jsons_dir.mkdir(parents=True)
    data = {"ignore": []}
    with open(import_map, "w") as f:
        json.dump(data, f, indent=4)
