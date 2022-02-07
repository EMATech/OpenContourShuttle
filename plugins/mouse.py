# This Python file uses the following encoding: utf-8
#
# SPDX-FileCopyrightText: 2021-2022 Raphaël Doursenaud <rdoursenaud@free.fr>
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""Mouse responder plugin"""

from pynput.mouse import Controller, Button

from plugins import ShuttleResponderPlugin


class MouseResponder(ShuttleResponderPlugin):
    mouse: Controller

    def __init__(self) -> None:
        super().__init__()
        self.mouse = Controller()

    ##
    # Absolute movement
    ##
    def move(self, x: int, y: int) -> None:
        self.mouse.position((x, y))

    def move_x(self, x: int) -> None:
        _y = self.mouse.position[1]
        self.mouse.position((x, _y))

    def move_y(self, y: int) -> None:
        _x = self.mouse.position[0]
        self.mouse.position((_x, y))

    ##
    # Relative movement
    ##
    def rel_move(self, x: int, y: int) -> None:
        self.mouse.move(x, y)

    def rel_move_x(self, x: int) -> None:
        self.mouse.move(x, 0)

    def rel_move_y(self, y: int) -> None:
        self.mouse.move(0, y)

    ##
    # Buttons
    ##
    def press_left_button(self) -> None:
        self.mouse.press(Button.left)

    def press_right_button(self) -> None:
        self.mouse.press(Button.right)

    def release_left_button(self) -> None:
        self.mouse.release(Button.left)

    def release_right_button(self) -> None:
        self.mouse.release(Button.right)

    def click_left_button(self) -> None:
        self.mouse.click(Button.left)

    def click_right_button(self) -> None:
        self.mouse.click(Button.right)

    def double_click_left_button(self) -> None:
        self.mouse.click(Button.left, 2)

    def double_click_right_button(self) -> None:
        self.mouse.click(Button.right, 2)

    def n_click_left_button(self, n) -> None:
        self.mouse.click(Button.left, n)

    def n_click_right_button(self, n) -> None:
        self.mouse.click(Button.right, n)

    ##
    # Scroll wheel
    ##
    def scroll(self, d, s) -> None:
        self.mouse.scroll(d, s)

    def scroll_up(self, s=1) -> None:
        self.mouse.scroll(0, s)

    def scroll_down(self, s=1) -> None:
        self.mouse.scroll(1, s)

    # TODO: Handle middle button
    # TODO: Handle more buttons?


if __name__ == "__main__":
    from device import ShuttleXpress
    from plugins import ShuttleBroker

    shuttle: ShuttleXpress = ShuttleXpress()

    broker_observer: ShuttleBroker = ShuttleBroker()
    shuttle.attach(broker_observer)

    shuttle.connect()
    while True:
        shuttle.poll()
