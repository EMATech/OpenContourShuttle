# This Python file uses the following encoding: utf-8
#
# SPDX-FileCopyrightText: 2021-2022 Raphaël Doursenaud <rdoursenaud@free.fr>
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""Keyboard responder plugin"""

from pynput.keyboard import Controller, Key

from plugins import ShuttleResponderPlugin


class KeyboardResponder(ShuttleResponderPlugin):
    keyboard: Controller

    def __init__(self) -> None:
        super().__init__()
        self.keyboard = Controller()

    def save(self):
        key = 's'
        with self.keyboard.pressed(Key.ctrl):
            self.keyboard.press(key)
            self.keyboard.release(key)


if __name__ == "__main__":
    from device import ShuttleXpress
    from plugins import ShuttleBroker

    shuttle: ShuttleXpress = ShuttleXpress()

    broker_observer: ShuttleBroker = ShuttleBroker()
    shuttle.attach(broker_observer)

    shuttle.connect()
    while True:
        shuttle.poll()
