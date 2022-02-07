# This Python file uses the following encoding: utf-8
#
# SPDX-FileCopyrightText: 2021-2022 Raphaël Doursenaud <rdoursenaud@free.fr>
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""Plugins broker system"""

from __future__ import annotations

import logging
from abc import ABC

from device import ShuttleXpressObserver, ShuttleXpressSubject, ConnectionEvent, DisconnectionEvent, RotaryEvent, \
    ButtonEvent, Wheel, Dial, Button

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger()


class ShuttleResponderPlugin:
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


class ShuttlePluginSample1(ShuttleResponderPlugin):
    def do_a(self) -> None:
        logger.debug("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        logger.debug("Component 1 does B.")
        self.mediator.notify(self, "B")


class ShuttlePluginSample2(ShuttleResponderPlugin):
    def do_c(self) -> None:
        logger.debug("Component 2 does C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        logger.debug("Component 2 does D.")
        self.mediator.notify(self, "D")


class ShuttleMediator(ABC):
    """
    The Mediator interface declares a method used by components to notify the
    mediator about various events. The Mediator may react to these events and
    pass the execution to other components  14
    """

    def notify(self, sender: object, event: str) -> None:
        pass


class ShuttleBroker(ShuttleXpressObserver, ShuttleMediator):
    def __init__(self) -> None:
        # plugins = enumerate()
        # for plugin in plugins:
        #    pass
        component1: ShuttlePluginSample1 = ShuttlePluginSample1()
        component2: ShuttlePluginSample2 = ShuttlePluginSample2()
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

        from mouse import MouseResponder
        self.mouse = MouseResponder()
        self.mouse.mediator = self

        from keyboard import KeyboardResponder
        self.keyboard = KeyboardResponder()
        self.keyboard.mediator = self

    def update(self, subject: ShuttleXpressSubject) -> None:
        logger.debug(f"{self.__class__.__name__}: Received event!")
        for event in subject.events:
            logger.debug(f"{event.__class__.__name__}")
            if isinstance(event, ConnectionEvent):
                logger.debug("Broker reacts on Connection event and triggers following operations:")
                self._component2.do_c()
            elif isinstance(event, DisconnectionEvent):
                logger.debug("Broker reacts on Disconnection event and triggers following operations:")
                self._component1.do_b()
                self._component2.do_c()
            elif isinstance(event, RotaryEvent):
                self._handle_rotary_event(event)
            elif isinstance(event, ButtonEvent):
                self._handle_button(event.element)
            else:
                logger.warning(f"{self.__class__.__name__}: Unsupported event type: {type(event)}")

    def _handle_rotary_event(self, event: RotaryEvent) -> None:
        if type(event.element) is Wheel:
            self.mouse.rel_move_y(event.value)
        elif type(event.element) is Dial:
            self.mouse.rel_move_x(event.value)

    def _handle_button(self, button: Button) -> None:
        if button.num == 3:
            self.keyboard.save()


def enumerate():
    # TODO: detect and import plugins automatically (Enabled/Disabled by configuration?)
    raise NotImplementedError


if __name__ == "__main__":
    from device import ShuttleXpress

    shuttle: ShuttleXpress = ShuttleXpress()

    broker_observer: ShuttleBroker = ShuttleBroker()
    shuttle.attach(broker_observer)

    shuttle.connect()
    while True:
        shuttle.poll()
