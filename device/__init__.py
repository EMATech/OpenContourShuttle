# SPDX-FileCopyrightText: 2021-2022 Raphaël Doursenaud <rdoursenaud@free.fr>
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
`Contour ShuttleXpress`
================================================================================

A multiplatform userland driver, configuration editor, event management & generator for Contour ShuttleXpress.

Contour, ShuttleXpress and ShuttlePro are trademarks of
Contour Innovations LLC in the United States.

These are not active trademarks in the European Union and France where I reside.

* Author(s): Raphaël Doursenaud <rdoursenaud@free.fr>

Implementation Notes
--------------------

    HID report
    ----------

    HID device (vID=0x0b33, pID=0x0020,v=0x0201); Contour Design; ShuttleXpress, Path: \\?\hid#vid_0b33&pid_0020#a&2c3e917c&0&0000#{4d1e55b2-f16f-11cf-88cb-001111000030

      Path:      \\?\hid#vid_0b33&pid_0020#a&2c3e917c&0&0000#{4d1e55b2-f16f-11cf-88cb-001111000030}

      Instance:  HID\VID_0B33&PID_0020\A&2C3E917C&0&0000

      Port (ID): 29

      Port (str):USB\VID_0B33&PID_0020\9&10B4E550&0&3

HID device documentation report
===============================

Top Level Details
-----------------

    Manufacturer String:    Contour Design
    Product Sting:          ShuttleXpress
    Serial Number:

    Vendor ID:              0x0b33
    Product ID:             0x0020
    Version number:         0x0201

    Device Path:            \\?\hid#vid_0b33&pid_0020#a&2c3e917c&0&0000#{4d1e55b2-f16f-11cf-88cb-001111000030}
    Device Instance Id:     HID\VID_0B33&PID_0020\A&2C3E917C&0&0000
    Parent Instance Id:     29

    Top level usage:        Page=0x000c, Usage=0x01
    Usage identification:   Consumer device, Consumer Control usage
    Link collections:       2 collection(shuttle)

Reports
-------

    Input Report
    ~~~~~~~~~~~~
    Length:     6 byte(shuttle)
    Buttons:    1 button(shuttle)
    Values:     2 value(shuttle)

    Output Report
    ~~~~~~~~~~~~~
    length:     0 byte(shuttle)
    Buttons:    0 button(shuttle)
    Values:     0 value(shuttle)

    Feature Report
    ~~~~~~~~~~~~~
    Length:     0 byte(shuttle)
    Buttons:    0 button(shuttle)
    Values:     0 value(shuttle)

    *** Input Caps ***

        Usage Range 1~13 (0x1~0xd), Page 0x9 (Button)
            bit_field: 2
            data_index_max: 14
            data_index_min: 2
            designator_max: 0
            designator_min: 0
            is_absolute: 1
            is_alias: 0
            is_button: True
            is_designator_range: 0
            is_range: 1
            is_string_range: 0
            is_value: False
            link_collection: 1
            link_usage: 0 (0x0)
            link_usage_page: 12 (0xc)
            report_id: 0
            string_max: 0
            string_min: 0

        Usage 56 (0x38), Page 0x1
        (Generic Desktop device, Wheel usage)
            bit_field: 6
            bit_size: 8
            data_index: 0
            designator_index: 0
            has_null: 0
            is_absolute: 0
            is_alias: 0
            is_button: False
            is_designator_range: 0
            is_range: 0
            is_string_range: 0
            is_value: True
            link_collection: 1
            link_usage: 0 (0x0)
            link_usage_page: 12 (0xc)
            logical_max: 127
            logical_min: -128
            physical_max: 0
            physical_min: 0
            report_count: 1
            report_id: 0
            string_index: 0
            units: 0
            units_exp: 0

        Usage 55 (0x37), Page 0x1
        (Generic Desktop device, Dial usage)
            bit_field: 46
            bit_size: 8
            data_index: 1
            designator_index: 0
            has_null: 0
            is_absolute: 0
            is_alias: 0
            is_button: False
            is_designator_range: 0
            is_range: 0
            is_string_range: 0
            is_value: True
            link_collection: 1
            link_usage: 0 (0x0)
            link_usage_page: 12 (0xc)
            logical_max: 255
            logical_min: 0
            physical_max: 0
            physical_min: 0
            report_count: 1
            report_id: 0
            string_index: 0
            units: 0
            units_exp: 0

Raw data_from_hid
-----------------

Wheel
~~~~~

- Encoder: 15 position with center rest  and 7 positions on each side
- Position: byte 1 (2nd)
- Length: 1 byte
- Range: 8-bit signed integer (-128 to 127)

    pos_center =  [0, 0, xx, 0, 0, 0]
    pos_minus_7 = [0, 249, xx, 0, 0, 0]
    pos_minus_6 = [0, 250, xx, 0, 0, 0]
    pos_minus_5 = [0, 251, xx, 0, 0, 0]
    pos_minus_4 = [0, 252, xx, 0, 0, 0]
    pos_minus_3 = [0, 253, xx, 0, 0, 0]
    pos_minus_2 = [0, 254, xx, 0, 0, 0]
    pos_minus_1 = [0, 255, xx, 0, 0, 0]
    pos_plus_1 = [0, 1, xx, 0, 0, 0]
    pos_plus_2 = [0, 2, xx, 0, 0, 0]
    pos_plus_3 = [0, 3, xx, 0, 0, 0]
    pos_plus_4 = [0, 4, xx, 0, 0, 0]
    pos_plus_5 = [0, 5, xx, 0, 0, 0]
    pos_plus_6 = [0, 6, xx, 0, 0, 0]
    pos_plus_7 = [0, 7, xx, 0, 0, 0]

Dial
~~~~

- Encoder: 10 ticks per full rotation
- Position: byte 2 (3rd)
- Length: 1 byte
- Range: 8-bit unsigned integer  (0-255)

Counts positive when rotated clockwise and negative the other way around on xx [0-255].
The value wraps around.

There’s a strange quirk in the hardware that makes it ignore the first tick when changing directions.

Buttons
~~~~~~~

- Position: byte 4-5
- Length: 2 bytes
- Values: bitfield (0 is released, 1 is pressed)

          B3
     B2        B4
    B1          B5

    B1_on_press = [0, 0, xx, 0, 16, 0]
    B2_on_press = [0, 0, xx, 0, 32, 0]
    B3_on_press = [0, 0, xx, 0, 64, 0]
    B4_on_press = [0, 0, xx, 0, 128, 0]
    B5_on_press = [0, 0, xx, 0, 0, 1]

**Multiple button presses**

Simply add the bitfield values.

Unused bytes
~~~~~~~~~~~~

Byte 0 and 3 appear unused.

My guess is the 3rd byte is used on the Pro model.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Union, Optional

import hid

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/EMATech/ContourShuttleXpress.git"

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger()


class Wheel:
    _pos: int

    centered: bool

    @property
    def pos(self) -> int:
        if self._pos is not None:
            return self._pos

    @pos.setter
    def pos(self, pos: int) -> None:
        if pos not in range(-7, 8):  # Filter only valid positions
            raise ValueError(f"Value {pos} was not expected. "
                             f"Please file a bug report: "
                             f"https://github.com/EMATech/ContourShuttleXpress/issues")

        # 0 is central position.
        self.centered = False
        if pos == 0:
            self.centered = True

        self._pos = pos

    def __init__(self) -> None:
        # Assumes initial state is centered
        self._pos = 0
        self.centered = True


class Dial:
    _pos: Optional[int]

    @property
    def pos(self) -> int:
        if self._pos is not None:
            return self._pos

    @pos.setter
    def pos(self, pos: int) -> None:
        if not 0 <= pos <= 255:  # Filter only valid values
            raise ValueError

        self._pos = pos

    def __init__(self) -> None:
        self._pos = None


class Button:
    _num: int

    push: bool = False

    @property
    def num(self) -> int:
        return self._num

    @num.setter
    def num(self, num: int) -> None:
        if not 1 <= num <= 5:  # Filter only valid values. TODO: change for Pro?
            raise ValueError

    def __init__(self, num: int) -> None:
        self._num = num
        self.push = False


class Event(ABC):
    element: Union[hid.device, Wheel, Dial, Button]
    desc: str  # Human-readable event description

    def __init__(self, element: Union[hid.device, Wheel, Dial, Button]) -> None:
        self.element = element


class ConnectionEvent(Event):
    def __init__(self, device: hid.device):
        super().__init__(device)
        self.desc = f"{device.get_manufacturer_string()} {device.get_product_string()} connected"


class DisconnectionEvent(Event):
    def __init__(self, device: hid.device):
        super().__init__(device)
        self.desc = f"{device.get_manufacturer_string()} {device.get_product_string()} disconnected"


class RotaryEvent(Event):
    element: Union[Wheel, Dial]

    _delta: int  # Delta
    _direction: bool  # True means up

    @property
    def direction(self) -> bool:
        return self._direction

    @direction.setter
    def direction(self, direction: bool) -> None:
        self.desc = f"{type(self.element).__name__} up" if direction \
            else f"{type(self.element).__name__} down"
        self._direction = direction

    @property
    def value(self) -> int:
        return self._delta

    @value.setter
    def value(self, val: int) -> None:
        self._delta = val

    def __init__(self, element: Union[Wheel, Dial], value: int, direction: bool) -> None:
        super().__init__(element)
        self.value = value
        self.direction = direction


class ButtonEvent(Event):
    element: Button

    def __init__(self, element: Button) -> None:
        super().__init__(element)
        self.desc = f"{type(element).__name__} {element.num} down" if element.push \
            else f"{type(element).__name__} {element.num} up"


class ShuttleXpressSubject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """
    events: list[Event]

    @abstractmethod
    def attach(self, observer: ShuttleXpressObserver) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: ShuttleXpressObserver) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ShuttleXpressObserver(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: ShuttleXpressSubject) -> None:
        """
        Receive update from subject.
        """
        pass


class ShuttleXpress(ShuttleXpressSubject):
    USB_VID: int = 0x0b33  # Contour Design, Inc.
    USB_PID_XPRESS: int = 0x0020  # ShuttleXpress
    USB_PID_PROV2: int = 0x0030  # ShuttlePRo v2 TODO: add support?
    HID_DATA_SIZE: int = 48

    # USB HID Device
    hid_device: hid.device
    connected: bool = False  # Missing from hid.device class

    # State
    _wheel: Wheel
    _dial: Dial
    _prev_dial_dir: Optional[bool] = None  # Needed to implement hardware quirk
    # TODO: Replace by list?
    _button1: Button
    _button2: Button
    _button3: Button
    _button4: Button
    _button5: Button

    # Event observation
    _observers: list[ShuttleXpressObserver] = []

    events: list[Event] = []

    @property
    def wheel(self) -> Wheel:
        return self._wheel

    @wheel.setter
    def wheel(self, new_pos: int) -> None:
        delta: Optional[int] = None
        logger.debug(f"{self.__class__.__name__}: Wheel position: {new_pos}")
        if self._wheel.pos != new_pos:
            delta = new_pos - self._wheel.pos
        self._wheel.pos = new_pos
        if delta:
            direction: bool = True if delta == 1 else False
            logger.info(f"{self.__class__.__name__}: Wheel position changed by {delta}")
            self.events.append(RotaryEvent(self.wheel, delta, direction))

    @property
    def dial(self) -> Dial:
        return self._dial

    @dial.setter
    def dial(self, new_pos: int) -> None:
        delta: Optional[int] = None
        logger.debug(f"{self.__class__.__name__}: Dial position: {new_pos}")
        if self._dial.pos is not None:
            if self._dial.pos != new_pos:
                delta = new_pos - self._dial.pos
                # Handle special cases when wrapping
                if delta == -255:
                    delta = 1
                elif delta == 255:
                    delta = -1
        self._dial.pos = new_pos
        if delta:
            direction: bool = True if delta == 1 else False
            dir_changed: bool = False if self._prev_dial_dir == direction else True
            self._prev_dial_dir = direction
            if dir_changed:
                delta = delta * 2  # Hardware quirk: misses one tick when changing directions
            logger.info(f"{self.__class__.__name__}: Dial position changed by {delta}")
            self.events.append(RotaryEvent(self.dial, delta, direction))

    @property
    def button1(self) -> Button:
        return self._button1

    @button1.setter
    def button1(self, new_state: bool) -> None:
        if self._button1.push != new_state:
            logger.info(f"{self.__class__.__name__}: Button 1 state changed!")
            self._button1.push = new_state
            self.events.append(ButtonEvent(self.button1))

    @property
    def button2(self) -> Button:
        return self._button2

    @button2.setter
    def button2(self, new_state: bool) -> None:
        if self._button2.push != new_state:
            logger.info(f"{self.__class__.__name__}: Button 2 state changed!")
            self._button2.push = new_state
            self.events.append(ButtonEvent(self.button2))

    @property
    def button3(self) -> Button:
        return self._button3

    @button3.setter
    def button3(self, new_state: bool) -> None:
        if self._button3.push != new_state:
            logger.info(f"{self.__class__.__name__}: Button 3 state changed!")
            self._button3.push = new_state
            self.events.append(ButtonEvent(self.button3))

    @property
    def button4(self) -> Button:
        return self._button4

    @button4.setter
    def button4(self, new_state: bool) -> None:
        if self._button4.push != new_state:
            logger.info(f"{self.__class__.__name__}: Button 4 state changed!")
            self._button4.push = new_state
            self.events.append(ButtonEvent(self.button4))

    @property
    def button5(self) -> Button:
        return self._button5

    @button5.setter
    def button5(self, new_state: bool) -> None:
        if self._button5.push != new_state:
            logger.info(f"{self.__class__.__name__}: Button 5 state changed!")
            self._button5.push = new_state
            self.events.append(ButtonEvent(self.button5))

    @classmethod
    def find(cls) -> list[dict]:
        logger.debug(f"{cls.__name__}: Listing all HID devices...")
        devices: list[dict] = hid.enumerate()
        shuttle_devices: list[dict] = []
        for dev in devices:
            logger.debug(f"{cls.__name__}: Found HID device: {dev}")
            if dev['vendor_id'] == ShuttleXpress.USB_VID and \
                    dev['product_id'] == ShuttleXpress.USB_PID_XPRESS:
                shuttle_devices.append(dev)
        logger.info(f"{cls.__name__}: Found {len(shuttle_devices)} "
                    f"Contour ShuttleXpress HID: {shuttle_devices}")
        return shuttle_devices

    def __init__(self) -> None:
        logger.debug(f"{self.__class__.__name__}: Instanciation.")
        self.hid_device = hid.device()
        self.connected = False
        self._wheel = Wheel()
        self._dial = Dial()
        self._button1 = Button(1)
        self._button2 = Button(2)
        self._button3 = Button(3)
        self._button4 = Button(4)
        self._button5 = Button(5)

    def __del__(self) -> None:
        logger.debug(f"{self.__class__.__name__}: Destruction.")
        if self.connected:
            self.events.append(DisconnectionEvent(self.hid_device))
        self.hid_device.close()
        self.connected = False
        self.notify()

    def connect(self, path: Optional[str] = None) -> None:
        if path:
            try:
                self.hid_device.open_path(path)

                logger.info(f"{self.__class__.__name__}: Connected to {self.hid_device.get_product_string()}!")

            except IOError as e:
                logger.error(f"{self.__class__.__name__}: Device not found: {e}")
                return
        else:
            try:
                self.hid_device.open(self.USB_VID, self.USB_PID_XPRESS)

                logger.info(f"{self.__class__.__name__}: Connected to {self.hid_device.get_product_string()}!")

            except IOError as e:
                logger.error(f"{self.__class__.__name__}: Device not found: {e}")
                return

        self.connected = True
        self.hid_device.set_nonblocking(True)

        self.events.append(ConnectionEvent(self.hid_device))
        self.notify()

    def poll(self) -> None:
        if not self.connected:
            self.connect()
            return
        else:
            try:
                data: list[int] = self.hid_device.read(self.HID_DATA_SIZE)
            except (OSError, ValueError) as e:
                logger.error(f"{self.__class__.__name__}: Could not read from device {e}")
                self.__del__()
                return

        if data:
            logger.debug(f"{self.__class__.__name__}: Data red from HID: {data!r}")
            self.wheel = int.from_bytes(data[0].to_bytes(1, 'big'), 'big', signed=True)
            self.dial = data[1]
            self.button1 = bool(data[3] & (1 << 4))
            self.button2 = bool(data[3] & (1 << 5))
            self.button3 = bool(data[3] & (1 << 6))
            self.button4 = bool(data[3] & (1 << 7))
            self.button5 = bool(data[4] & (1 << 0))
            self.notify()

    ##
    # Observers management
    ##
    def attach(self, observer: ShuttleXpressObserver) -> None:
        logger.debug(f"{self.__class__.__name__}: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: ShuttleXpressObserver) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        logger.debug(f"{self.__class__.__name__}: Notifying observers...")
        for observer in self._observers:
            observer.update(self)
        self.events.clear()


class ShuttleXpressObserverSample(ShuttleXpressObserver):
    def update(self, subject: ShuttleXpressSubject) -> None:
        logger.debug(f"{self.__class__.__name__}: State changed!")
        for event in subject.events:
            logger.info(f"{self.__class__.__name__}: {event.desc}")
            if isinstance(event, ConnectionEvent):
                self._handle_connection(event.element)
            elif isinstance(event, DisconnectionEvent):
                self._handle_disconnection(event)
            elif isinstance(event, RotaryEvent):
                self._handle_rotary_event(event)
            elif isinstance(event, ButtonEvent):
                self._handle_button(event.element)
            else:
                logger.warning(f"{self.__class__.__name__}: Unsupported event type: {type(event)}")

    @classmethod
    def _handle_connection(cls, device: hid.device) -> None:
        logger.info(f"{cls.__name__}: Connected to {device.get_manufacturer_string()} {device.get_product_string()}")

    @classmethod
    def _handle_disconnection(cls, event: DisconnectionEvent) -> None:
        logger.info(f"{cls.__name__}: Disconnected.")

    def _handle_rotary_event(self, event: RotaryEvent) -> None:
        if type(event.element) is Wheel:
            self._handle_wheel(event.element, event.direction, event.value)
        elif type(event.element) is Dial:
            self._handle_dial(event.element, event.direction, event.value)

    @classmethod
    def _handle_wheel(cls, wheel: Wheel, direction: bool, value: int) -> None:
        if direction:
            logger.info(f"{cls.__name__}: Wheel up by {value}")
        else:
            logger.info(f"{cls.__name__}: Wheel down by {value}!")
        if wheel.centered:
            logger.info(f"{cls.__name__}: Wheel centered!")
        logger.info(f"{cls.__name__}: Wheel position: {wheel.pos}")

    @classmethod
    def _handle_dial(cls, dial: Dial, direction: bool, value: int) -> None:
        if direction:
            logger.info(f"{cls.__name__}: Dial up by {value}!")
        else:
            logger.info(f"{cls.__name__}: Dial down by {value}!")
        logger.info(f"D{cls.__name__}: ial position: {dial.pos}")

    @classmethod
    def _handle_button(cls, button: Button) -> None:
        state: str = 'down' if button.push else 'up'
        logger.info(f"{cls.__name__}: Button {button.num} state changed to: {state}!")


if __name__ == '__main__':
    shuttle: ShuttleXpress = ShuttleXpress()

    sample_observer: ShuttleXpressObserver = ShuttleXpressObserverSample()
    shuttle.attach(sample_observer)

    shuttle.connect()
    while True:
        shuttle.poll()
