from pypp_python.interfaces import ABC, abstractmethod
from pypp_python import Val, dataclass


class GreeterInterface(ABC):
    @abstractmethod
    def greet(self, a: int):
        pass


@dataclass
class GreeterImpl(GreeterInterface):
    name: Val[str]

    def greet(self, a: int):
        print(f"{self.name} says hello {a} times!")


def interface_with_dataclasses_fn():
    print("INTERFACE WITH DATACLASSES RESULTS:")
    g: GreeterImpl = GreeterImpl("Alice")
    g.greet(3)
