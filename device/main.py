"""
HID report
----------

HID device (vID=0x0b33, pID=0x0020, v=0x0201); Contour Design; ShuttleXpress, Path: \\?\hid#vid_0b33&pid_0020#a&2c3e917c&0&0000#{4d1e55b2-f16f-11cf-88cb-001111000030}

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
import copy
import logging

import hid

SHUTTLEPROV2_PID = 0x0030  # TODO: add support?

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger()


class ShuttleXpressConnection(object):
    DATA_SIZE = 48

    def __init__(self, desc: dict):
        self.desc = desc
        self.device = hid.device()
        self.shuttle = ShuttleXpress()
        self.state = ShuttleXpressState(self.shuttle)

    def connect(self):
        try:
            # h.open(CONTOUR_VID, SHUTTLEXPRESS_PID)  # Only opens first shuttle
            self.device.open_path(self.desc['path'])

            logger.info("%s found!" % self.device.get_product_string())

            while True:
                data = self.device.read(self.DATA_SIZE)
                self.shuttle.update(data_from_hid=data)
                self.state.update(self.shuttle)

        except IOError:
            logger.error("Connection not found!")
            pass

        finally:
            self.device.close()


class ShuttleXpress(object):
    USB_VID = 0x0b33
    USB_PID = 0x0020

    def __init__(self):
        self.wheel_position = 0  # Signed  int from -127 to 128. 0 is central position. Values [-120, -1] and [8, 128) are invalid.
        self.dial_position = 0  # Unsigned int (Counter to 255)
        self.button1_pressed = False
        self.button2_pressed = False
        self.button3_pressed = False
        self.button4_pressed = False
        self.button5_pressed = False

    def update(self, wheel_pos=0, dial_pos=0, button1=False, button2=False, button3=False, button4=False,
               button5=False, data_from_hid=None):

        if data_from_hid is not None:
            logger.debug("Data from HID: %r", data_from_hid)
            self.wheel_position = int.from_bytes(data_from_hid[0].to_bytes(1, 'big'), 'big', signed=True)
            self.dial_position = data_from_hid[1]
            self.button1_pressed = bool(data_from_hid[3] & (1 << 4))
            self.button2_pressed = bool(data_from_hid[3] & (1 << 5))
            self.button3_pressed = bool(data_from_hid[3] & (1 << 6))
            self.button4_pressed = bool(data_from_hid[3] & (1 << 7))
            self.button5_pressed = bool(data_from_hid[4] & (1 << 0))
        else:
            self.wheel_position = wheel_pos
            self.dial_position = dial_pos
            self.button1_pressed = button1
            self.button2_pressed = button2
            self.button3_pressed = button3
            self.button4_pressed = button4
            self.button5_pressed = button5

        logger.debug("Wheel position: %s", self.wheel_position)
        logger.debug("Dial position: %s", self.dial_position)
        logger.debug("Button 1 pressed: %s", self.button1_pressed)
        logger.debug("Button 2 pressed: %s", self.button2_pressed)
        logger.debug("Button 3 pressed: %s", self.button3_pressed)
        logger.debug("Button 4 pressed: %s", self.button4_pressed)
        logger.debug("Button 5 pressed: %s", self.button5_pressed)


class ShuttleXpressState(object):
    current_state = ShuttleXpress
    previous_state = ShuttleXpress

    def __init__(self, state: ShuttleXpress):
        self.current_state = copy.copy(state)
        self.previous_state = None

    def update(self, state: ShuttleXpress):
        self.previous_state = self.current_state
        self.current_state = copy.copy(state)
        self._state_changed()

    def _state_changed(self):
        logger.debug("State changed!")
        if self.current_state.wheel_position != self.previous_state.wheel_position:
            self._wheel_state_changed()
        if self.current_state.dial_position != self.previous_state.dial_position:
            self._dial_state_changed()
        if self.current_state.button1_pressed != self.previous_state.button1_pressed:
            self._button1_state_changed()
        if self.current_state.button2_pressed != self.previous_state.button2_pressed:
            self._button2_state_changed()
        if self.current_state.button3_pressed != self.previous_state.button3_pressed:
            self._button3_state_changed()
        if self.current_state.button4_pressed != self.previous_state.button4_pressed:
            self._button4_state_changed()
        if self.current_state.button5_pressed != self.previous_state.button5_pressed:
            self._button5_state_changed()

    def _wheel_state_changed(self):
        logger.debug("Wheel state changed!")
        # TODO: fire callback?
        if self.current_state.wheel_position == 0:
            self._wheel_center()
        if self.current_state.wheel_position > self.previous_state.wheel_position:
            self._wheel_up()
        else:
            self._wheel_down()

    def _wheel_center(self):
        logger.debug("Wheel center!")
        # TODO: fire callback

    def _wheel_up(self):
        logger.debug("Wheel up!")
        # TODO: fire callback

    def _wheel_down(self):
        logger.debug("Wheel down!")
        # TODO: fire callback

    def _dial_state_changed(self):
        logger.debug("Dial state changed!")
        # TODO: fire callback
        if (self.current_state.dial_position > self.previous_state.dial_position) \
                or (self.current_state.dial_position == 0 and self.previous_state.dial_position == 255) \
                and not (self.current_state.dial_position == 255 and self.previous_state.dial_position == 0):
            self._dial_up()
        else:
            self._dial_down()

    def _dial_up(self):
        logger.debug("Dial up!")
        # TODO: fire callback

    def _dial_down(self):
        logger.debug("Dial down!")
        # TODO: fire callback

    def _button1_state_changed(self):
        logger.debug("Button 1 state changed!")
        # TODO: fire callback
        if self.current_state.button1_pressed:
            self._button1_down()
        else:
            self._button1_up()

    def _button1_down(self):
        logger.debug("Button 1 down!")
        # TODO: fire callback

    def _button1_up(self):
        logger.debug("Button 1 up!")
        # TODO: fire callback

    def _button2_state_changed(self):
        logger.debug("Button 2 state changed!")
        # TODO: fire callback
        if self.current_state.button2_pressed:
            self._button2_down()
        else:
            self._button2_up()

    def _button2_down(self):
        logger.debug("Button 2 down!")
        # TODO: fire callback

    def _button2_up(self):
        logger.debug("Button 2 up!")
        # TODO: fire callback

    def _button3_state_changed(self):
        logger.debug("Button 3 state changed!")
        # TODO: fire callback
        if self.current_state.button3_pressed:
            self._button3_down()
        else:
            self._button3_up()

    def _button3_down(self):
        logger.debug("Button 3 down!")
        # TODO: fire callback

    def _button3_up(self):
        logger.debug("Button 3 up!")
        # TODO: fire callback

    def _button4_state_changed(self):
        logger.debug("Button 4 state changed!")
        # TODO: fire callback
        if self.current_state.button4_pressed:
            self._button4_down()
        else:
            self._button4_up()

    def _button4_down(self):
        logger.debug("Button 4 down!")
        # TODO: fire callback

    def _button4_up(self):
        logger.debug("Button 4 up!")
        # TODO: fire callback

    def _button5_state_changed(self):
        logger.debug("Button 5 state changed!")
        # TODO: fire callback
        if self.current_state.button5_pressed:
            self._button5_down()
        else:
            self._button5_up()

    def _button5_down(self):
        logger.debug("Button 5 down!")
        # TODO: fire callback

    def _button5_up(self):
        logger.debug("Button 5 up!")
        # TODO: fire callback


def find_shuttle_devices():
    logger.debug("Listing all HID devices...")
    devices_desc = hid.enumerate()
    shuttle_hid_devices_desc = []
    for dev_desc in devices_desc:
        logger.debug("Found HID device: %s", dev_desc)
        if dev_desc['vendor_id'] == ShuttleXpress.USB_VID and dev_desc['product_id'] == ShuttleXpress.USB_PID:
            shuttle_hid_devices_desc.append(dev_desc)
    logger.debug("Found %data Contour ShuttleXpress HID: %s", len(shuttle_hid_devices_desc), shuttle_hid_devices_desc)
    return shuttle_hid_devices_desc


if __name__ == '__main__':
    shuttle_devices_desc = find_shuttle_devices()
    if not shuttle_devices_desc:
        logger.error("No Shuttle HID device found!")
        exit(0)
    if len(shuttle_devices_desc) > 1:
        logger.warning("More than one Shuttle HID found. Not supported (yet).")
        # TODO: implement multiple Shuttle HIDs support?
        raise NotImplementedError
    shuttle_dev_desc = shuttle_devices_desc[0]  # Let’s pick the first
    conn = ShuttleXpressConnection(shuttle_dev_desc)
    conn.connect()
