from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(frozen=True, slots=True)
class MetadataSaver:
    _write_metadata_to_dir: str | None
    _namespace: str | None
    _python_dir: Path

    def save_if_required(self):
        if self._write_metadata_to_dir is not None:
            assert self._namespace is not None, (
                "Namespace must be set to write metadata. Either set namespace or set "
                "write_metadata_to_dir to null."
            )
            metadata_file = (
                self._python_dir / self._write_metadata_to_dir / "metadata.json"
            )
            with open(metadata_file, "w") as f:
                json.dump({"namespace": self._namespace}, f, indent=2)
