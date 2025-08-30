from pathlib import Path


def create_py_executable(target_dir: Path) -> Path:
    return target_dir / "python" / ".venv" / "Scripts" / "python.exe"
