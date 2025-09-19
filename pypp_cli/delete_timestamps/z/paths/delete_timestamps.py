from pathlib import Path


def create_timestamps_file(target_dir: Path) -> Path:
    return target_dir / ".pypp" / "file_timestamps.json"
