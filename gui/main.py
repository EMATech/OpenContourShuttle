# This Python file uses the following encoding: utf-8
#
# SPDX-FileCopyrightText: 2021 Raphaël Doursenaud <rdoursenaud@free.fr>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
`Open Contour Shuttle GUI`
================================================================================

A multiplatform configuration editor, event management & generator GUI for Contour ShuttleXpress.

Contour, ShuttleXpress and ShuttlePro are trademarks of
Contour Innovations LLC in the United States.

These are not active trademarks in the European Union and France where I reside.

* Author(s): Raphaël Doursenaud <rdoursenaud@free.fr>

Implementation Notes
--------------------

"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/EMATech/ContourShuttleXpress.git"

import logging
from platform import python_version
from typing import Dict, List, Optional

import PySide6
from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QSystemTrayIcon
from qt_material import QtStyleTools

from device import Button, ButtonEvent, ConnectionEvent, Dial, \
    DisconnectionEvent, Event, RotaryEvent, ShuttleXpress, \
    ShuttleXpressObserver, ShuttleXpressSubject, Wheel
from mainwindow_ui import Ui_MainWindow


##
# Logging system
##


class LogSignal(QObject):
    signal = Signal(str, logging.LogRecord)


class LogHandler(logging.Handler):
    def __init__(self, slotfunc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.signaller = LogSignal()
        self.signaller.signal.connect(slotfunc)

    def emit(self, record):
        s = self.format(record)
        self.signaller.signal.emit(s, record)


##
# Device communication
##

class ShuttleSignals(QObject):
    data = Signal(object)


shuttle_signals = ShuttleSignals()


class GuiObserver(ShuttleXpressObserver):
    def update(self, subject: ShuttleXpressSubject) -> None:
        for event in subject.events:
            shuttle_signals.data.emit(event)


class ShuttleWorker(QThread):
    active: bool = True
    finished: bool = False

    def __init__(self, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)
        self.shuttle = ShuttleXpress()
        self.shuttle.attach(GuiObserver())
        self.shuttle.connect()

    def run(self) -> None:
        while self.active:
            self.shuttle.poll()
        self.finished = True

    def stop(self) -> None:
        del self.shuttle
        self.active = False


##
# GUI
##


class GUI(QMainWindow, Ui_MainWindow, QtStyleTools):
    ICON: QIcon
    TITLE: str = "Open Contour Shuttle"
    WHEEL_MAP: Dict[int, QObject]
    BUTTON_MAP: List[QObject]
    LOG_COLORS = {
        logging.DEBUG: 'lightgray',
        logging.INFO: 'white',
        logging.WARNING: 'orange',
        logging.ERROR: 'red',
        logging.CRITICAL: 'purple',
    }

    def __init__(self) -> None:
        super().__init__()

        # self.load_ui()  # Broken
        # Use pyside-uic form.ui > gui.py to generate the UI instead
        self.setupUi(self)

        # Hide ASAP to avoid window flash
        self.about_widget.setHidden(True)
        self.plugins_widget.setHidden(True)
        self.config_widget.setHidden(True)
        self.log_widget.setHidden(True)

        h = LogHandler(self.append_log)
        fs = '%(levelname)-8s %(message)s'
        formatter = logging.Formatter(fs)
        h.setFormatter(formatter)
        logging.getLogger().addHandler(h)

        self.ICON = QIcon('images/icon.png')

        self.WHEEL_MAP = {
            -7: self.wheel_neg7,
            -6: self.wheel_neg6,
            -5: self.wheel_neg5,
            -4: self.wheel_neg4,
            -3: self.wheel_neg3,
            -2: self.wheel_neg2,
            -1: self.wheel_neg1,
            0: self.wheel_cent0,
            1: self.wheel_pos1,
            2: self.wheel_pos2,
            3: self.wheel_pos3,
            4: self.wheel_pos4,
            5: self.wheel_pos5,
            6: self.wheel_pos6,
            7: self.wheel_pos7,
        }
        self.BUTTON_MAP = [None, self.button_1, self.button_2, self.button_3, self.button_4, self.button_5]

        self.setWindowIcon(self.ICON)
        self.setWindowTitle(self.TITLE)
        #self.set_ms_windows_icon()
        extra = {
            # Button colors
            'danger': '#dc3545',
            'warning': '#ffc107',
            'success': '#17a2b8',

            # Font
            'font_family': 'Roboto',
        }
        self.apply_stylesheet(self, theme='dark_red.xml', extra=extra)

        # self.setWindowFlags(self.windowFlags() | Qt.Dialog | Qt.MSWindowsFixedSizeDialogHint)
        # self.statusbar.setSizeGripEnabled(False)

        self.update_status_bar("Connecting...")

        self.show()

        if QSystemTrayIcon.isSystemTrayAvailable():
            self.systray = QSystemTrayIcon()
            self.systray.setIcon(self.ICON)
            systray_menu = QMenu(title=self.TITLE, parent=self)
            quit_action = QAction("&Quit", self)
            systray_menu.addAction(quit_action)
            quit_action.triggered.connect(self.close)
            self.systray.setContextMenu(systray_menu)
            self.systray.setVisible(True)
            self.systray.activated.connect(self.handle_systray_activation)

        shuttle_signals.data.connect(self.handle_events)
        self.shuttle_worker = ShuttleWorker()
        self.shuttle_worker.start()
        self.shuttle_worker.finished.connect(self.shuttle_worker.quit)

        self.about_text.setMarkdown(f"""
Open Contour Shuttle
====================

A multiplatform userland driver, configuration editor, event manager & generator
for Contour ShuttleXpress & ShuttlePRO v2.

Version: `{__version__}`

Source: `{__repo__}`

Running on Python v{python_version()}

Legal notice
------------

### License

Copyright 2021 Raphaël Doursenaud

This software is released under the terms of the GNU General Public License,
version 3.0 or later (GPL-3.0-or-later).

### Dependencies & License Acknowledgment

**Python**

Used under the terms of the PSF License Agreement.

**libusb hidapi**

Copyright Alan Ott, Signal 11 Software.  
Used under the terms of the GNU General Public License, version 3.0 (GPL-3.0).

**Trezor cython-hidapi**  

Copyright Pavol Rusnak, SatoshiLabs.  
Used under the terms of the GNU General Public License, version 3.0 (GPL-3.0).

**Qt PySide6**

Used under the terms of the GNU Lesser General Public License v3.0 (LGPL-3.0).

**UN-GCPDS Qt-Material**

Used under the BSD-2-Clause License.

**Material Design Icons**

Used under the Pictogrammers Free License.

### Trademarks

Contour, ShuttleXpress and ShuttlePro are trademarks of
Contour Innovations LLC in the United States of America.

These are not registered or active trademarks in the European Union and
France where I reside.
""")
        self.about_button.clicked.connect(self.toggle_about_vis)
        self.plug_button.clicked.connect(self.toggle_plugins_vis)
        self.conf_button.clicked.connect(self.toggle_config_vis)
        self.log_button.clicked.connect(self.toggle_log_vis)
        self.log_clear_button.clicked.connect(self.clear_log)

    # def load_ui(self):
    #    loader = QUiLoader()
    #    path = os.path.join(os.path.dirname(__file__), "mainwindow.ui")
    #    ui_file = QFile(path)
    #    ui_file.open(QFile.ReadOnly)
    #    print(ui_file.readAll())
    #    loader.load(ui_file, self)
    #    ui_file.close()

    def handle_systray_activation(self, reason: QSystemTrayIcon.ActivationReason) -> None:
        if reason is QSystemTrayIcon.ActivationReason.Trigger:
            self.toggle_main_window_visibility()

    def toggle_main_window_visibility(self) -> None:
        self.hide() if self.isVisible() else self.show()

    def update_status_bar(self, message: str) -> None:
        self.statusbar.showMessage(message)

    def toggle_about_vis(self) -> None:
        self.about_widget.setVisible(self.about_widget.isHidden())

    def toggle_config_vis(self) -> None:
        self.config_widget.setVisible(self.config_widget.isHidden())

    def toggle_plugins_vis(self) -> None:
        self.plugins_widget.setVisible(self.plugins_widget.isHidden())

    def toggle_log_vis(self) -> None:
        self.log_widget.setVisible(self.log_widget.isHidden())

    @Slot(str, logging.LogRecord)
    def append_log(self, message, record):
        color = self.LOG_COLORS.get(record.levelno, 'black')
        s = f'<pre><font color="{color}">{message}</font></pre>'
        self.log_text.appendHtml(s)

    def clear_log(self) -> None:
        self.log_text.clear()

    def handle_events(self, event: Event) -> None:
        self.update_status_bar(event.desc)
        if isinstance(event, ConnectionEvent):
            self.usb_status.setChecked(True)
        elif isinstance(event, DisconnectionEvent):
            self.usb_status.setChecked(False)
        #       self.shuttle_worker.stop()
        elif isinstance(event, RotaryEvent):
            self.handle_rotary_event(event)
        elif isinstance(event, ButtonEvent):
            self.handle_button(event.element)

    def handle_rotary_event(self, rotary_event: RotaryEvent) -> None:
        if type(rotary_event.element) is Wheel:
            self.handle_wheel(rotary_event.element, rotary_event.direction, rotary_event.value)
        elif type(rotary_event.element) is Dial:
            self.handle_dial(rotary_event.element, rotary_event.direction, rotary_event.value)

    def handle_wheel(self, wheel: Wheel, direction: bool, change: int) -> None:
        self.WHEEL_MAP[wheel.pos].setChecked(True)

    def handle_dial(self, dial: Dial, direction: bool, change: int) -> None:
        self.dial.setValue(self.dial.value() + change)

    def handle_button(self, button: Button) -> None:
        self.BUTTON_MAP[button.num].setChecked(button.push)

    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        self.shuttle_worker.stop()

    @staticmethod
    def set_ms_windows_icon() -> None:
        """
        Force Microsoft Windows to properly display the application icon in the task bar

        Workaround from: https://stackoverflow.com/a/27872625
        """
        try:
            import ctypes
            myappid = u'eu.ematech.contour.shuttlexpress'  # arbitrary string
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except AttributeError as e:
            logging.warning(f"{e}")
            pass

    @staticmethod
    def set_mac_os_title() -> None:
        """
        Force Mac OS X to properly display the app name in the title bar using PyObjC

        Workaround from: https://stackoverflow.com/a/54755290
        """
        try:
            from Foundation import NSBundle
            bundle = NSBundle.mainBundle()
            if bundle:
                app_name = GUI.TITLE
                app_info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
                if app_info:
                    app_info['CFBundleName'] = app_name
        except ImportError as e:
            logging.warning(f"{e}")
            pass


if __name__ == "__main__":
    import platform
    import sys

    ###
    # Platform idiosyncrasies
    ###
    currentplatform = platform.system()
    if currentplatform == 'Windows':
        GUI.set_ms_windows_icon()
    elif currentplatform == 'Darwin':
        GUI.set_mac_os_title()
    app = QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec())
