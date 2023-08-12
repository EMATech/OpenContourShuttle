"""Mediator"""

from __future__ import annotations

from abc import ABC


class ShuttleMediator(ABC):
    """
    The Mediator interface declares a method used by components to notify the
    mediator about various events. The Mediator may react to these events and
    pass the execution to other components.
    """

    def notify(self, sender: object, event: str) -> None:
        pass


class ShuttleBroker(ShuttleMediator):
    def __init__(self, component1: ShuttlePluginSample1, component2: ShuttlePluginSample2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


class ShuttlePlugin(ABC):
    """
    The Base Component provides the basic functionality of storing a mediator's
    instance inside component objects.
    """

    def __init__(self, mediator: ShuttleMediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> ShuttleMediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: ShuttleMediator) -> None:
        self._mediator = mediator


"""
Concrete Components implement various functionality. They don't depend on other
components. They also don't depend on any concrete mediator classes.
"""


class ShuttlePluginSample1(ShuttlePlugin):
    def do_a(self) -> None:
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")
        self.mediator.notify(self, "B")


class ShuttlePluginSample2(ShuttlePlugin):
    def do_c(self) -> None:
        print("Component 2 does C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self.mediator.notify(self, "D")


if __name__ == "__main__":
    # The client code.
    c1 = ShuttlePluginSample1()
    c2 = ShuttlePluginSample2()
    mediator = ShuttleBroker(c1, c2)

    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    c2.do_d()
