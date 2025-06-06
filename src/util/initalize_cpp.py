import os
import shutil
from src.config import C_CPP_TEMPLATE_DIR, C_CPP_DIR


def initialize_cpp_project() -> bool:
    # Create the target directory if it doesn't exist
    if not os.path.exists(C_CPP_DIR):
        print(f"Creating C++ project directory at: {C_CPP_DIR}")
        os.makedirs(C_CPP_DIR)

        # Copy files and directories from the template
        for item in os.listdir(C_CPP_TEMPLATE_DIR):
            src_path = os.path.join(C_CPP_TEMPLATE_DIR, item)
            dst_path = os.path.join(C_CPP_DIR, item)
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path)
            else:
                shutil.copy2(src_path, dst_path)
        return True
    return False
