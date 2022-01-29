"""
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
--------

### Wheel

1st byte (1 byte, range signed integer -128 to 127)

(7 positions + and 7 positions minus, center rest)

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


### Dial

2nd byte (1 byte, range int 0-255)
Counts positive when rotated clockwise and negative the other way around on xx [0-255]

### Buttons

Bitfields on 4th and 5th bytes (2 bytes, 1 == pressed)

      B3
 B2        B4
B1          B5

B1_on_press = [0, 0, xx, 0, 16, 0]
B2_on_press = [0, 0, xx, 0, 32, 0]
B3_on_press = [0, 0, xx, 0, 64, 0]
B4_on_press = [0, 0, xx, 0, 128, 0]
B5_on_press = [0, 0, xx, 0, 0, 1]

Multiple button presses:
simply add the 5th field values (Bitfield)
"""
from __future__ import annotations

import logging
from abc import ABC, abstractmethod
# from numpy import int8, uint8
from typing import List, Union

import hid

# from device.control import Control
# from mouse import MouseControl

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger()


class Wheel:
    _pos: Union[None, int]  # FIXME: use int8?
    centered = True

    @property
    def pos(self) -> int:
        if self._pos is not None:
            return self._pos

    @pos.setter
    def pos(self, pos: int) -> None:
        # Signed int from -127 to 128.
        if not -127 <= pos <= 128:
            raise ValueError(f"Value {pos} is not between -127 and 128")

        # 0 is central position.
        self.centered = False
        if pos == 0:
            self.centered = True

        self._pos = pos

    def __init__(self) -> None:
        self._pos = None


class Dial:
    _pos: Union[None, int]  # FIXME: use uint8?

    @property
    def pos(self) -> int:
        if self._pos is not None:
            return self._pos

    @pos.setter
    def pos(self, pos: int) -> None:
        # Unsigned int (Wrapping counter from 0 to 255)
        if not 0 <= pos <= 255:
            # FIXME: autowrap with a warning?
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
        if not 1 <= num <= 5:
            raise ValueError

    def __init__(self, num: int) -> None:
        self._num = num
        self.push = False


class Event(ABC):
    name: str  # Human-readable event name
    element: Union[hid.device, Wheel, Dial, Button]

    def __init__(self, element: Union[hid.device, Wheel, Dial, Button]) -> None:
        self.element = element


class ConnectionEvent(Event):
    def __init__(self, device: hid.device):
        super().__init__(device)
        self.name = f"{device.get_manufacturer_string()}"


class RotaryEvent(Event):
    element: Union[Wheel, Dial]

    _delta: int  # Delta
    _direction: bool  # True means up

    @property
    def direction(self) -> bool:
        return self._direction

    @property
    def value(self) -> int:
        return self._delta

    @value.setter
    def value(self, val: int) -> None:
        direction = True if val >= 0 else False
        self.name = f"{type(self.element).__name__} up" if direction \
            else f"{type(self.element).__name__} down"
        self._delta = val
        self._direction = direction

    def __init__(self, element: Union[Wheel, Dial], value: int) -> None:
        super().__init__(element)
        self.value = value


class ButtonEvent(Event):
    element: Button

    def __init__(self, element: Button) -> None:
        super().__init__(element)
        self.name = f"{type(element).__name__} {element.num} down" if element.push \
            else f"{type(element).__name__} {element.num} up"


class ShuttleXpressSubject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    events: List[Event]

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
    USB_VID = 0x0b33  # Contour Design, Inc.
    USB_PID = 0x0020  # ShuttleXpress
    SHUTTLEPROV2_PID = 0x0030  # TODO: add support?
    DATA_SIZE = 48

    # USB HID Device
    usb_descriptor: dict
    hid_device: hid.device

    # State
    _wheel: Wheel
    _dial: Dial
    # TODO: Replace by list?
    _button1: Button
    _button2: Button
    _button3: Button
    _button4: Button
    _button5: Button

    _observers: List[ShuttleXpressObserver] = []

    events: List[Event] = []

    @property
    def wheel(self) -> Wheel:
        return self._wheel

    @wheel.setter
    def wheel(self, new_pos: int) -> None:
        delta = None
        logger.debug(f"{self.__class__.__name__}: New wheel position: {new_pos}")
        if self._wheel.pos is not None:
            if self._wheel.pos != new_pos:
                delta = new_pos - self._wheel.pos
                logger.debug(f"{self.__class__.__name__}: Wheel position changed by {delta}")
        self._wheel.pos = new_pos
        if delta:
            self.events.append(RotaryEvent(self.wheel, delta))

    @property
    def dial(self) -> Dial:
        return self._dial

    @dial.setter
    def dial(self, new_pos: int) -> None:
        delta = None
        logger.debug(f"{self.__class__.__name__}: New dial position: {new_pos}")
        if self._dial.pos is not None:
            if self._dial.pos != new_pos:
                delta = new_pos - self._dial.pos
                logger.debug(f"{self.__class__.__name__}: Dial position changed by {delta}")
        self._dial.pos = new_pos
        if delta:
            self.events.append(RotaryEvent(self.dial, delta))

    @property
    def button1(self) -> Button:
        return self._button1

    @button1.setter
    def button1(self, new_state: bool) -> None:
        if self._button1.push != new_state:
            logger.debug(f"{self.__class__.__name__}: Button 1 state changed!")
            self._button1.push = new_state
            self.events.append(ButtonEvent(self.button1))

    @property
    def button2(self) -> Button:
        return self._button2

    @button2.setter
    def button2(self, new_state: bool) -> None:
        if self._button2.push != new_state:
            logger.debug(f"{self.__class__.__name__}: Button 2 state changed!")
            self._button2.push = new_state
            self.events.append(ButtonEvent(self.button2))

    @property
    def button3(self) -> Button:
        return self._button3

    @button3.setter
    def button3(self, new_state: bool) -> None:
        if self._button3.push != new_state:
            logger.debug(f"{self.__class__.__name__}: Button 3 state changed!")
            self._button3.push = new_state
            self.events.append(ButtonEvent(self.button3))

    @property
    def button4(self) -> Button:
        return self._button4

    @button4.setter
    def button4(self, new_state: bool) -> None:
        if self._button4.push != new_state:
            logger.debug(f"{self.__class__.__name__}: Button 4 state changed!")
            self._button4.push = new_state
            self.events.append(ButtonEvent(self.button4))

    @property
    def button5(self) -> Button:
        return self._button5

    @button5.setter
    def button5(self, new_state: bool) -> None:
        if self._button5.push != new_state:
            logger.debug(f"{self.__class__.__name__}: Button 5 state changed!")
            self._button5.push = new_state
            self.events.append(ButtonEvent(self.button5))

    @staticmethod
    def find() -> List[dict]:
        logger.debug(f"{ShuttleXpress.__class__.__name__}: Listing all HID devices...")
        devices_desc = hid.enumerate()
        shuttle_hid_devices_desc = []
        for dev_desc in devices_desc:
            logger.debug(f"{ShuttleXpress.__class__.__name__}: Found HID device: %s", dev_desc)
            if dev_desc['vendor_id'] == ShuttleXpress.USB_VID and dev_desc['product_id'] == ShuttleXpress.USB_PID:
                shuttle_hid_devices_desc.append(dev_desc)
        logger.debug(f"{ShuttleXpress.__class__.__name__}: Found %data Contour ShuttleXpress HID: %s",
                     len(shuttle_hid_devices_desc),
                     shuttle_hid_devices_desc)
        return shuttle_hid_devices_desc

    def __init__(self) -> None:
        self.hid_device = hid.device()
        self._wheel = Wheel()
        self._dial = Dial()
        self._button1 = Button(1)
        self._button2 = Button(2)
        self._button3 = Button(3)
        self._button4 = Button(4)
        self._button5 = Button(5)

    def __del__(self) -> None:
        self.hid_device.close()

    def connect_first(self) -> None:
        devices_desc = self.find()
        if not devices_desc:
            logger.error("No Shuttle HID device found!")
            exit(0)
        if len(devices_desc) > 1:
            logger.warning("More than one Shuttle HID found. This is not yet supported.")
            # TODO: implement multiple Shuttle HIDs support?
            # raise NotImplementedError

        self.connect(devices_desc[0])  # Let’s pick the first

    def connect(self, desc: dict) -> None:
        self.usb_descriptor = desc
        try:
            # h.open(CONTOUR_VID, SHUTTLEXPRESS_PID)  # Only opens first shuttle
            self.hid_device.open_path(self.usb_descriptor['path'])

            logger.info("%s found!" % self.hid_device.get_product_string())

        except IOError:
            logger.error("Connection not found!")

        self.hid_device.set_nonblocking(True)

        self.events.append(ConnectionEvent(self.hid_device))
        self.notify()

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

    def poll(self) -> None:
        data = self.hid_device.read(self.DATA_SIZE)

        if data:
            logger.debug(f"{self.__class__.__name__}: Data from HID: %r", data)
            self.wheel = int.from_bytes(data[0].to_bytes(1, 'big'), 'big', signed=True)
            self.dial = data[1]
            self.button1 = bool(data[3] & (1 << 4))
            self.button2 = bool(data[3] & (1 << 5))
            self.button3 = bool(data[3] & (1 << 6))
            self.button4 = bool(data[3] & (1 << 7))
            self.button5 = bool(data[4] & (1 << 0))
            self.notify()


class ShuttleXpressObserverSample(ShuttleXpressObserver):

    def update(self, subject: ShuttleXpressSubject) -> None:
        logger.debug(f"{self.__class__.__name__}: State changed!")
        for event in subject.events:
            logger.info(f"{self.__class__.__name__}: {event.name}")
            if isinstance(event, ConnectionEvent):
                self._handle_connection(event.element)
            elif isinstance(event, RotaryEvent):
                self._handle_rotary_event(event)
            elif isinstance(event, ButtonEvent):
                self._handle_button(event.element)
            else:
                logger.warning(f"Unsupported event type: {type(event)}")

    @staticmethod
    def _handle_connection(device: hid.device) -> None:
        logger.info(f"Connected to {device.get_manufacturer_string()} {device.get_product_string()}")

    def _handle_rotary_event(self, rotary_event: RotaryEvent) -> None:
        if type(rotary_event.element) is Wheel:
            self._handle_wheel(rotary_event.element, rotary_event.direction, rotary_event.value)
        elif type(rotary_event.element) is Dial:
            self._handle_dial(rotary_event.element, rotary_event.direction, rotary_event.value)

    @staticmethod
    def _handle_wheel(wheel: Wheel, direction: bool, value: int) -> None:
        if direction:
            logger.info(f"Wheel up by {value}")
        else:
            logger.info(f"Wheel down by {value}!")
        if wheel.centered:
            logger.info("Wheel center!")
        logger.info(f"Wheel position: {wheel.pos}")

    @staticmethod
    def _handle_dial(dial: Dial, direction: bool, value: int) -> None:
        if direction:
            logger.info(f"Dial up by {value}!")
        else:
            logger.info(f"Dial down by {value}!")
        logger.info(f"Dial position: {dial.pos}")

    @staticmethod
    def _handle_button(button: Button) -> None:
        state = 'down' if button.push else 'up'
        logger.debug(f"Button {button.num} state changed to: {state}!")


if __name__ == '__main__':
    shuttle = ShuttleXpress()

    sample_observer = ShuttleXpressObserverSample()
    shuttle.attach(sample_observer)

    while True:
        shuttle.poll()
