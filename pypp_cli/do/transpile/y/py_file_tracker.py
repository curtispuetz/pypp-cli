from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class PyFilesTracker:
    all_files: list[Path]
    main_files: set[Path]

    def handle_deleted_files(self, deleted_files: list[Path]):
        for deleted_file in deleted_files:
            if deleted_file in self.main_files:
                self.main_files.remove(deleted_file)
