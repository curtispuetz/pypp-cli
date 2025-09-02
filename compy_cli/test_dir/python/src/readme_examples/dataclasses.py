from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Greeter:
    name: str
    prefix: str

    def greet(self) -> str:
        return f"Hello, {self.prefix} {self.name}!"
