Contour ShuttleXpress
=====================

A multiplatform userland driver, configuration editor, event manager & generator for Contour ShuttleXpress.

![GUI prototype](GUIprototype.png)


Status
------

Proof of concept!

Welcoming any contributions, especially:

- comments
- tests: particularly on platforms other than Microsoft Windows or versions earlier than 11
- providing access to currently unsupported hardware:
    - ShuttlePRO v2

Features / TODO list
--------------------

- [ ] Platform support
    - [x] Microsoft Windows
        - [x] GUI
        - [x] Tray icon shortcut to GUI
        - [ ] Run as a [windows service](http://thepythoncorner.com/dev/how-to-create-a-windows-service-in-python/)?
        - [ ] Add configurator to control panel?
    - [x] Apple Mac OS X
    - [ ] GNU/Linux
    - [ ] Android?
    - [ ] Apple iOS/iPadOS?

- [x] State management engine
    - [x] Find and open device
        - [x] USB HID via hidapi
    - [x] Decode raw values
        - [x] Observer pattern Events
    - [ ] **(WIP)** Central broker
    - [ ] Responders plugin system


- [ ] **(WIP)** GUI
    - [x] Qt6 via PySide6
    - [X] Main window
    - [x] Icon
    - [x] Title
    - [x] System tray icon
    - [x] Display state graphically
    - [x] Status
        - [x] Connection
        - [x] Events
    - [x] ~~Menu?~~
    - [x] About window
    - [x] Log window
        - [x] Aggregate & display logs
        - [x] Clear logs
        - [ ] Write logs to file
    - [ ] Configuration UI
        - [ ] Generate configurations
        - [ ] Load existing configurations
        - [ ] Write/Store configurations
    - [ ] Emulation mode when no hardware is connected
    - [ ] Separate from the engine
    - [ ] Custom graphical widgets?
        - [ ] Wheel (Rotating image with color tick)
        - [ ] Dial (Rotating image)
        - [ ] Button (Depict depressed state)

### Events

State changes.

- [x] USB:
    - [x] connected
    - [x] disconnected
- [x] Buttons 1 to 5:
    - [x] press
    - [x] release
- [x] Wheel:
    - [x] centered (position 0)
    - [x] position change (-7 to 7)
    - [x] direction: up
    - [x] direction: down
- [x] Dial:
    - [x] direction: up
    - [x] direction: down
    - [x] absolute position (0 to 255)

### Observers

Gets notified upon events

- [x] GUI
- [ ] **(WIP)** Responder plugins Broker

### Broker

Maps events observation to responses depending on the current configuration and available responder plugins.

- [ ] Configuration system
    - [ ] Formats support
        - [ ] Custom?
            - [ ] Comments
        - [ ] [Official driver configurations](https://contourdesign.fr/support/windows-shuttle-settings/)
            - [ ] Parse
            - [ ] Generate
    - [ ] macros (generate multiple events)

- [ ] Responder plugins
    - [ ] API specification
    - [ ] Sample implementation

- [ ] runtime profiles support
    - [ ] configure multiple profiles
        - [ ] default global
        - [ ] named
            - [ ] (optional) linked to one or more specific external states:
                - [ ] application in focus
                - [ ] current desktop/monitor?
                - [ ] session/user?
                - [ ] external trigger event?
    - [ ] (auto?) switch profiles dynamically
        - [ ] using buttons
        - [ ] detect running application
            - [ ] Microsoft Windows
                - [ ] win32ui
            - [ ] Mac OS X
            - [ ] GNU/Linux

### Responders

Plugin based system.

Generates external events triggered by the broker.

- [ ] **(POC)** generate keyboard strokes and/or modifiers
    - [x] ~~SendKeys?~~
    - [x] ~~pywin32 shell.SendKeys?~~
    - [ ] **(POC)** pynput! (Also support mouse)
    - [ ] Frequency (Once/Hold…)

- [ ] **(POC)** generate mouse events
    - [ ] **(POC)** pynput! (Also support mouse)
    - [ ] click
    - [ ] wheel

- [ ] generate MIDI
    - [ ] Arbitrary (User defined)
    - [ ] MCU compatible
    - [ ] HUI compatible

- [ ] generate OSC

- [ ] call APIs?

- [ ] launch applications
    - ?

Contour format settings
-----------------------

May be used as samples for interoperability.

### Contour

- [Microsoft Windows](https://www.contourdesign.com/windows-shuttle-settings/)
- [Mac OS X](https://www.contourdesign.com/mac-shuttle-settings/)

### GitHub

- [ShuttleProSettings](https://github.com/Rolias/ShuttleProSettings)
    - Camtasia Studio 8 *Microsoft Windows*
    - Reaper *Apple Mac OS X*
- [camtasia-shuttlepro-settings](https://github.com/digitaldrummerj/camtasia-shuttlepro-settings/blob/master/Camtasia%20Studio%209.pref)
    - Camtasia Studio 9 *Microsoft Windows*

Similar and/or related projects
---------------------------


<!-- BEGIN Template

### []()



- Language: 
- License: 
- OS: 
- Dependencies: 

END Template -->

### [Contour-ShuttlePRO-V1-Linux-Custom-Implementation](https://github.com/c0deous/Contour-ShuttlePRO-V1-Linux-Custom-Implementation)

A simple barebones driver written in Python for the Contour ShuttlePRO V1 Control Surface.

- Language: Python
- License: Unspecified/Proprietary (Copyright 2016 c0deous?)
- OS: GNU/Linux
- Dependencies: python-evdev

### [cncjs-pendant-shuttle](https://github.com/bensuffolk/cncjs-pendant-shuttle)

A cncjs pendant to connect a Contour Design ShuttleXpress to the raspberry pi that is running cncjs.

- Language: Javascript/NodeJS
- License: MIT (Copyright (c) 2021 Ben Suffolk)
- OS: GNU/Linux
- Dependencies: udev, cnjs, shuttle-control-usb

### [kh750remote](https://github.com/floxch/kh750remote)

Neumann KH 750 DSP remote control with Contour ShuttleXpress.

- Language: Javascript/NodeJS
- License: MIT (Copyright (c) 2021 floxch)
- OS: Multiplatform?
- Dependencies: multicast-dns, node-hid, node-notifier, node-osc

### [LightroomShuttlePro](https://github.com/abrilevskiy/LightroomShuttlePro)

Lightroom plugin for support contourdesign ShuttlePro v2.

- Language: C++/Lua
- License: GPL-3.0  (Copyright 2018 abrilevskiy?) + Proprietary (Copyright (c) 2003 Contour Design, Inc. & Copyright
  2016 Adobe Systems Incorporated)
- OS: Microsoft Windows
- Dependencies: ShuttleSDK.dll

### [node-red-contrib-shuttlexpress](https://github.com/legacymachine/node-red-contrib-shuttlexpress)

Node-RED nodes for USB ShuttleXpress device.

- Language: Javascript/NodeJS
- License: MIT (Copyright (c) 2019 legacymachine aka Legacy Machine Works, LLC aka Josh Dudley)
- OS: Multiplatform
- Dependencies: node-hid

### [node-shuttlexpress](https://github.com/legacymachine/node-shuttlexpress)

NodeJS API for USB ShuttleXpress Device.

- Language: Javascript/NodeJS
- License: MIT (Copyright (c) 2019 legacymachine aka Legacy Machine Works, LLC aka Josh Dudley)
- OS: Multiplatform
- Dependencies: node-hid

### [shuttle](https://github.com/jeamland/shuttle)

A little Swift program to make a ShuttleXpress do what I want.

- Language: Swift
- License: BSD-2-Clause (Copyright (c) 2016, Benno Rice)
- OS: Apple Mac OS X
- Dependencies: Mac OS X 10.12 SDK

### [Shuttle](https://github.com/1div0/Shuttle)

Controlling Ardour with Open Sound Control from Contour Design ShuttlePRO & ShuttlePRO v2.

- Language: C
- License: GPL-2.0 (Copyright (C) 2001-2007 Dan Dennedy)
- OS: GNU/Linux
- Dependencies: liblo

### [shuttle-go](https://github.com/abourget/shuttle-go)

Contour Design Shuttle Pro V2 drivers for Linux, in Go, with modifiers and just more slick.

- Language: Go
- License: MIT (Copyright (c) 2017 Alexandre Bourget)
- OS: GNU/Linux
- Dependencies: udev

### [ShuttleControlUSB](https://github.com/hopejr/ShuttleControlUSB)

A Library to use Contour Design ShuttleXpress and ShuttlePro v2 in Node.js projects without the driver.

- Language: Javascript/NodeJS
- License: MIT (Copyright (c) 2020 James Hope)
- OS: Multiplatform?
- Dependencies: node-hid, usb-detection, udev

### [shuttled](https://github.com/Shamanon/shuttled)

ShuttlePro fork.

Daemon for Contour Shuttle devices to translate button/jogwheel events to keystrokes sent to uinput.

- Language: C
- License: GPL-3.0 (Copyright 2013 Eric Messick, Copyleft 2015 Joshua Besneatte)
- OS: GNU/Linux
- Dependencies: libx11, libxtst, udev, uinput

### [shuttleevent](https://github.com/pmjdebruijn/shuttleevent)

ShuttlePRO fork.

User program for interpreting key, shuttle, and jog events from a Contour Design ShuttlePRO v2

- Language: C
- License: GPL-3.0 (Copyright 2013 Eric Messick, Copyright 2018 Albert Graef, Copyright 2019 Pascal de Bruijn)
- OS: GNU/Linux
- Dependencies: libx11, libxtst, udev

### [ShuttleGRBL](https://github.com/Duffmann/ShuttleGRBL)

Contour's ShuttleExpress for jogging a GRBL CNC machine under cncjs and Linux using USB/hidraw.

- Language: Javascript/NodeJS
- License: MIT (Copyright (c) 2020 Duffmann aka Nelio Santos)
- OS: GNU/Linux
- Dependencies: commander, inquirer, jsonwebtoken, lodash.get, node-hid, serialport, socket.io-client, udev, vorpal

### [shuttleit](https://github.com/irontoby/shuttleit)

Event handler for Contour Design ShuttleXpress.

- Language: Perl
- License: Apache-2.0 (Copyright 2015 Tobias Johnson)
- OS: GNU/Linux
- Dependencies: udev

### [shuttlemidi](https://github.com/dg1psi/shuttlemidi)

Sends MIDI from the Shuttle Contour to SDR Console.

- Language: Go
- License: Apache-2.0 (Copyright 2021 dg1psi)
- OS: Multiplatform?
- Dependencies: hidapi, loopmidi

### [ShuttleNET](https://github.com/EddieMac74/ShuttleNET)

A simple .NET wrapper for the Contour Shuttle SDK. Written in C#.

- Language: C#
- License: Unspecified/Proprietary (Copyright © Edward MacDonald 2018)
- OS: Microsoft Windows?
- Dependencies: ShuttleSDK.dll

### [shuttlepro](https://github.com/russells-crockpot/shuttlepro)

A python app to allow usage of the Contour ShuttlePro V2 in Linux.

- Language: Python
- License: Unspecified/Proprietary (Copyright 2020 Brendan McGloin?)
- OS: GNU/Linux
- Dependencies: click, evdev, Xlib

### [ShuttlePRO](https://github.com/nanosyzygy/ShuttlePRO)

User program for interpreting key, shuttle, and jog events from a Contour Design ShuttlePRO v2.

- Language: C
- License: GPL-3.0 (Copyright 2013 Eric Messick)
- OS: GNU/Linux
- Dependencies: libx11, libxtst, udev

### [ShuttlePRO](https://github.com/SERVCUBED/ShuttlePRO)

ShuttlePRO fork.

User program for interpreting key, shuttle, and jog events from a Contour Design ShuttlePRO v2

- Language: C
- License: GPL-3.0 (Copyright 2013 Eric Messick, Copyright 2018 Albert Graef, Copyright 2020 Ben Blain)
- OS: GNU/Linux
- Dependencies: libjack, libx11, libxtst, udev

### [ShuttlePro-M](https://github.com/w5pny/ShuttlePRO-M)

ShuttlePro fork.

User program for interpreting key, shuttle, and jog events from a Contour Design ShuttlePRO v2.

- Language: C
- License: GPL-3.0 (Copyright 2013 Eric Messick, Copyright 2020 Harry G McGavran Jr)
- OS: GNU/Linux
- Dependencies: udev

### [shuttleprov2_linux_driver](https://github.com/rmt/shuttleprov2_linux_driver)

A Linux userspace "driver" for the ShuttlePro V2 device, and some tools to read events from a wacom tablet.

- Language: D
- License: LGPL-3.0 (Copyright 2013 Robert Thomson)
- OS: GNU/Linux
- Dependencies: None

### [shuttleroom](https://github.com/7Pass/shuttleroom)

Lightroom plugin to use ShuttleXpress controller for Develop.

- Language: C#
- License: Unspecified/Proprietary (Copyright 2020 Ngoc Van Tran?)
- OS: Microsoft Windows, Ubuntu?
- Dependencies: .NET Core 3.1.100, ShuttleSDK64.dll

### [shuttle-xpress-android](https://github.com/freshollie/shuttle-xpress-android)

Android Library for interfacing with a Contour Design Shuttle Xpress 🕹️.

- Language: Java
- License: Apache-2.0 (Copyright 2017 Oliver Bell)
- OS: Android
- Dependencies: API 17

### [ShuttleXpress](https://github.com/threedaymonk/shuttlexpress)

Use a Contour ShuttleXpress in Linux.

- Language: Scheme
- License: Unspecified/Proprietary (Copyright 2012 Paul Battley?)
- OS: GNU/Linux
- Dependencies: Xlib, udev

### [Shuttlexpress-MPD](https://github.com/matthew-wolf-n4mtt/shuttlexpress-mpd)

Shuttlexpress-MPD is a Music Player Daemon (MPD) client that uses a Contour ShuttleXpress to control the status of the
playback of an MPD instance.

- Language: C
- License: GPL-2.0 (Copyright 2019 Matthew J. Wolf)
- OS: GNU/Linux
- Dependencies: mpd, udev, systemd

### [widget-shuttlexpress](https://github.com/chilipeppr/widget-shuttlexpress)

The ShuttleXpress widget helps you setup your own ShuttleXpress jog dial USB device and enables audio feedback as you
toggle the buttons on the device.

- Language: Javascript/HTML/CSS
- License: Unspecified/Proprietary (Copyright 2016 John Lauer?)
- OS: ChiliPeppr
- Dependencies: ChiliPeppr

Development log
---------------

### Finding the right library for Microsoft Windows

#### Attempt 1

Using [pyUSB](https://pypi.org/project/pyusb/)

Can’t access device without a kernel driver.

Kernel driver has been generated using [libusb-win32](https://sourceforge.net/projects/libusb-win32/), but you need to
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

### Exploring patterns

Settled for an observer pattern with a central broker and separate plugin based responders.


Legal notice
------------

### License

Copyright 2021-2022 Raphaël Doursenaud

This software is released under the terms of the GNU General Public License, version 3.0 or later (GPL-3.0-or-later).

See [LICENSE](LICENSE).

### Dependencies & License Acknowledgment

- [Python](https://python.org) v3.10  
  Used under the terms of the PSF License Agreement.
- libusb [hidapi](https://github.com/libusb/hidapi)  
  Copyright Alan Ott, Signal 11 Software.  
  Used under the terms of the GNU General Public License, version 3.0 (GPL-3.0).
- via Trezor [cython-hidapi](https://github.com/trezor/cython-hidapi)  
  Copyright Pavol Rusnak, SatoshiLabs.  
  Used under the terms of the GNU General Public License, version 3.0 (GPL-3.0).
- Qt [PySide6](https://www.pyside.org)  
  Used under the terms of the GNU Lesser General Public License v3.0 (LGPL-3.0).
- UN-GCPDS [Qt-Material](https://github.com/UN-GCPDS/qt-material)  
  Used under the BSD-2-Clause License.
- [Material Design Icons](https://materialdesignicons.com)  
  Used under the Pictogrammers Free License.

### Trademarks

Contour, ShuttleXpress and ShuttlePro are trademarks of Contour Innovations LLC in the United States of America.

These are not registered or active trademarks in the European Union and France where I reside.

#### Other

Other trademarks are property of their respective owners and used fairly for descriptive and nominative purposes only.
