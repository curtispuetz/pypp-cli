from abc import ABC, abstractmethod


class _PrivateInterface(ABC):
    @abstractmethod
    def a(self):
        pass


class InterfaceClass(ABC):
    @abstractmethod
    def speak(self, a: int):
        pass

    @abstractmethod
    def talk(self) -> str:
        pass


class Impl1(InterfaceClass):
    def speak(self, a: int):
        print("number given:", a)

    def talk(self) -> str:
        return "hello"


class Impl2(InterfaceClass):
    def speak(self, a: int):
        print("number given times 2:", 2 * a)

    def talk(self) -> str:
        return "hello there"


def _fn_that_accepts_interface(i: InterfaceClass):
    i.speak(2)
    print(i.talk())


def interfaces_fn():
    print("INTERFACES RESULTS:")
    # basic
    a: Impl1 = Impl1()
    a.speak(42)
    print(a.talk())
    # second type
    b: Impl2 = Impl2()
    b.speak(43)
    # passing either type somewhere
    _fn_that_accepts_interface(a)
    _fn_that_accepts_interface(b)
