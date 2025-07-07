from dataclasses import dataclass


@dataclass
class OnlyHDataClass:
    field1: list[float]
    field2: dict[str, set[int]]
