import os
import shutil

from pypp_core.src.config import PyppDirs


def initialize_cpp_project(dirs: PyppDirs) -> bool:
    # Create the target directory if it doesn't exist
    if not os.path.exists(dirs.cpp_dir):
        print(f"Creating C++ project directory at: {dirs.cpp_dir}")
        os.makedirs(dirs.cpp_dir)

        # Copy files and directories from the template
        for item in os.listdir(dirs.cpp_template_dir):
            src_path = os.path.join(dirs.cpp_template_dir, item)
            dst_path = os.path.join(dirs.cpp_dir, item)
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path)
            else:
                shutil.copy2(src_path, dst_path)
        return True
    return False
