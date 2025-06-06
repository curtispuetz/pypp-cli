from pathlib import Path

from src.config import C_CPP_BUILD_RELEASE_DIR

exe_path = Path(C_CPP_BUILD_RELEASE_DIR) / "pyppDefaultExeName.exe"
print(exe_path)
print("Exists:", exe_path.exists())
