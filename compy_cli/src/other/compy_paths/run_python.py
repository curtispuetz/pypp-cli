from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class RunPythonCompyPaths:
    py_executable: Path
    python_src_dir: Path


def create_run_python_paths(target_dir: Path) -> RunPythonCompyPaths:
    return RunPythonCompyPaths(
        target_dir / "python" / ".venv" / "Scripts" / "python.exe",
        target_dir / "python" / "src",
    )
