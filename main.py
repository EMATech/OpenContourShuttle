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
Link collections:       2 collection(s)

Reports
-------

Input Report
~~~~~~~~~~~~
Length:     6 byte(s)
Buttons:    1 button(s)
Values:     2 value(s)

Output Report
~~~~~~~~~~~~~
length:     0 byte(s)
Buttons:    0 button(s)
Values:     0 value(s)

Feature Report
~~~~~~~~~~~~~
Length:     0 byte(s)
Buttons:    0 button(s)
Values:     0 value(s)

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
import logging

import hid

CONTOUR_VID = 0x0b33
SHUTTLEXPRESS_PID = 0x0020
SHUTTLEXPRESS_DATA_SIZE = 48

logging.basicConfig(level=logging.DEBUG)


class ShuttleXpress(object):
    wheel_position = 0  # Signed  int from -127 to 128. 0 is central position. Values [-120, -1] and [8, 128) are invalid.
    dial_position = 0  # Unsigned int (Counter to 255)
    button1_pressed = False
    button2_pressed = False
    button3_pressed = False
    button4_pressed = False
    button5_pressed = False

    def __init__(self, wheel_pos=0, dial_pos=0, button1=False, button2=False, button3=False, button4=False,
                 button5=False, data_from_hid=None):

        if data_from_hid is not None:
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
    previous_state: ShuttleXpress = None
    current_state: ShuttleXpress = None

    def __init__(self, state: ShuttleXpress = None):
        self.current_state = state

    def new_state(self, state: ShuttleXpress):
        if self.current_state is not None:
            self.previous_state = self.current_state
        self.current_state = state
        if self.previous_state is not None:
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
        if self.current_state.dial_position > self.previous_state.dial_position \
                or self.current_state.dial_position == 0 and self.previous_state.dial_position == 255:
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


if __name__ == '__main__':

    logger = logging.getLogger()

    logger.debug("Listing all HID devices...")
    devices = hid.enumerate()

    shuttles = []

    for dev in devices:
        logger.debug("Found HID device: %s", dev)
        if dev['vendor_id'] == CONTOUR_VID and dev['product_id'] == SHUTTLEXPRESS_PID:
            shuttles.append(dev)

    logger.debug("Found %d Contour ShuttleXpress: %s", len(shuttles), shuttles)

    if not shuttles:
        logger.error("Device not found!")
        exit(0)

    if len(shuttles) > 1:
        logger.warning("More than one device found. Not supported (yet).")
        # TODO: implement multiple devices support
        raise NotImplementedError

    dev = shuttles[0]  # Let’s pick the first

    try:
        h = hid.device()

        # h.open(CONTOUR_VID, SHUTTLEXPRESS_PID)  # Only opens first device

        h.open_path(dev['path'])

        logger.info("%s found!" % h.get_product_string())

        state = ShuttleXpressState()

        while True:
            d = h.read(SHUTTLEXPRESS_DATA_SIZE)
            s = ShuttleXpress(data_from_hid=d)
            state.new_state(s)

    except IOError:
        logger.error("Device not found!")
        pass

    h.close()
