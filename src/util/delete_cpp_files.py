import os
import shutil
from src.config import C_CPP_MAIN_FILE, C_CPP_SRC_DIR


def delete_cpp_main_and_src_dir():
    # Delete the C_CPP_MAIN_FILE if it exists
    if os.path.isfile(C_CPP_MAIN_FILE):
        os.remove(C_CPP_MAIN_FILE)
        print("Deleted main.cpp")

    # Delete the entire C_CPP_SRC_DIR if it exists
    if os.path.isdir(C_CPP_SRC_DIR):
        shutil.rmtree(C_CPP_SRC_DIR)
        print("Deleted src C++ files")
