from dataclasses import dataclass
import json
from pathlib import Path

from pypp_cli.do.transpile.z_i.proj_metadata import ProjMetadata


@dataclass(frozen=True, slots=True)
class MetadataSaver:
    _write_metadata_to_dir: str | None
    _namespace: str
    _python_dir: Path

    def save_if_required(self):
        if self._write_metadata_to_dir is not None:
            metadata = ProjMetadata(namespace=self._namespace)
            metadata_file = (
                self._python_dir / self._write_metadata_to_dir / "metadata.json"
            )
            with open(metadata_file, "w") as f:
                json.dump(metadata.model_dump(), f, indent=4)
