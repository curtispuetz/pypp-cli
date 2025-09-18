from abc import ABC, abstractmethod
from pypp_python import Valu, dataclass


class GreeterInterface(ABC):
    @abstractmethod
    def greet(self, a: int):
        pass


@dataclass
class GreeterImpl(GreeterInterface):
    name: Valu(str)

    def greet(self, a: int):
        print(f"{self.name} says hello {a} times!")


def interface_with_dataclasses_fn():
    print("INTERFACE WITH DATACLASSES RESULTS:")
    g: GreeterImpl = GreeterImpl("Alice")
    g.greet(3)
