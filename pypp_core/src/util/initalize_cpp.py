import os
import shutil
from importlib.resources import files, as_file

from pypp_core.src.config import PyppDirs


def initialize_cpp_project(dirs: PyppDirs) -> bool:
    # Create the target directory if it doesn't exist
    if not os.path.exists(dirs.cpp_dir):
        print(f"Creating C++ project directory at: {dirs.cpp_dir}")
        os.makedirs(dirs.cpp_dir)

        # Copy files and directories from the template
        template_root = files("pypp_core.data.cpp_template")
        for item in template_root.iterdir():
            with as_file(item) as src_path:
                dst_path = os.path.join(dirs.cpp_dir, item.name)
                if src_path.is_dir():
                    shutil.copytree(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)
        return True
    return False
