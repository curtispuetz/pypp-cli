class Greeter:
    def __init__(self, name: str, prefix: str):
        self.name = name
        self.prefix = prefix

    def greet(self) -> str:
        return f"Hello, {self.prefix} {self.name}!"
