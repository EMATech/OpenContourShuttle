Contour ShuttleXpress
=====================

An attempt at writing a userland driver in Python.

Features
--------

- [x] Find and open device (USB HID)

- [x] Decode raw values
    - [x] State management
    - [WIP] State change hooks/callbacks
        - [ ] Buttons [1-5]:
          - [ ] on_press()
          - [ ] on_release()
        - [ ] Wheel:
          - [ ] on_position() [-7, 7]
          - [ ] on_turn_up()
          - [ ] on_turn_down()
        - [ ] Dial:
          - [ ] on_turn_up()
          - [ ] on_turn_down()

- [ ] send keyboard strokes and/or modifiers
    - [ ] SendKeys?
    - [ ] pywin32 shell.SendKeys?
        - [ ] Frequency (Once/Hold…)
    - [ ] pynput! (Also support mouse)

- [ ] send mouse events
    - [ ] click
    - [ ] wheel

- [ ] send MIDI?

- [ ] call APIs?

- [ ] launch applications
    - ?

- [ ] per application profile
    - [ ] detect running application
        - [ ] Microsoft Windows
            - [ ] win32ui
        - [ ] Mac OS X
        - [ ] GNU/Linux
    - [ ] switch profile using buttons

- [ ] macros

- [ ] comments

- [ ] parse [official driver configurations](https://contourdesign.fr/support/windows-shuttle-settings/)

- [WIP] Configurator (GUI)
    - [x] Qt
    - [ ] Display state/debug
    - [ ] Load existing configurations
    - [ ] Generate configurations

- [ ] Plugins?

- [ ] Platforms support
    - [ ] Microsoft Windows
        - [ ] Run as a [windows service](http://thepythoncorner.com/dev/how-to-create-a-windows-service-in-python/) ?
        - [ ] Configurator in control panel?
        - [ ] (optional) Tray icon shortcut to configurator
    - [ ] Mac OS X
    - [ ] GNU/Linux
    - [ ] Android?
    - [ ] iOS/iPadOS?

Development log
---------------

###  Finding the right library for Microsoft Windows

#### Attempt 1

Using [pyUSB](https://pypi.org/project/pyusb/)

Can’t access device without a kernel driver.

Kernel driver has been generated using [libusb-win32](https://sourceforge.net/projects/libusb-win32/) but you need to 
disable driver signature enforcement before installing.

The easier way is to use [Zadig](https://zadig.akeo.ie/).

#### Attempt 2

Using [pyWinUSB](https://pypi.org/project/pywinusb/)

Can get HID without driver installation on Microsoft Windows!

Let’s continue…

Success!

But...

#### Attempt 3

Using [cython-hidapi](https://pypi.org/project/hidapi/)

Crossplatform (Microsoft Windows, Mac OS X, GNU/Linux)

Success on Microsoft Windows without prior driver installation!
Hope it’s the same on other platforms.

### Building a GUI

#### PySide6 (QT6)

Prototype UI done

![GUI prototype](GUIprototype.png)