# This Python file uses the following encoding: utf-8

import PySide6
import hid
from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu

from device import ShuttleXpress, ShuttleXpressObserver, ShuttleXpressSubject, Event, ButtonEvent, Button, \
    RotaryEvent, Wheel, Dial, ConnectionEvent
from mainwindow_ui import Ui_MainWindow


class ShuttleSignals(QObject):
    data = Signal(object)


shuttle_signals = ShuttleSignals()


class GUIobserver(ShuttleXpressObserver):
    def update(self, subject: ShuttleXpressSubject) -> None:
        for event in subject.events:
            shuttle_signals.data.emit(event)


class ShuttleWorker(QThread):
    active = True
    finished = False

    def __init__(self, parent=None):
        super().__init__(parent)
        self.shuttle = ShuttleXpress()
        self.shuttle.attach(GUIobserver())
        self.shuttle.connect_first()

    def run(self):
        while self.active:
            self.shuttle.poll()
        self.finished = True

    def stop(self):
        self.active = False


class GUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.ICON = QIcon('images/icon.png')
        self.TITLE = "Contour ShuttleXpress"

        # self.load_ui()  # Broken
        # Use pyside-uic form.ui > gui.py to generate the UI instead
        self.setupUi(self)

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
        self.setStyleSheet('''        
                            background-color: #262626;
                            color: #FFFFFF;
                            font-size: 11pt;
                ''')

        self.show()

        self.updateStatusBar("UI loaded!")

        if QSystemTrayIcon.isSystemTrayAvailable():
            self.systray = QSystemTrayIcon()
            self.systray.setIcon(self.ICON)
            systray_menu = QMenu(title=self.TITLE, parent=self)
            quit_action = QAction("&Quit", self)
            systray_menu.addAction(quit_action)
            quit_action.triggered.connect(self.close)
            self.systray.setContextMenu(systray_menu)
            self.systray.setVisible(True)

        self.updateStatusBar("Connecting...")
        shuttle_signals.data.connect(self.change)
        self.shuttle_worker = ShuttleWorker()
        self.shuttle_worker.start()
        self.shuttle_worker.finished.connect(self.shuttle_worker.quit)

    # def load_ui(self):
    #    loader = QUiLoader()
    #    path = os.path.join(os.path.dirname(__file__), "mainwindow.ui")
    #    ui_file = QFile(path)
    #    ui_file.open(QFile.ReadOnly)
    #    print(ui_file.readAll())
    #    loader.load(ui_file, self)
    #    ui_file.close()

    def updateStatusBar(self, message):
        self.statusbar.showMessage(message)

    def change(self, event: Event):
        if isinstance(event, ConnectionEvent):
            self.handle_connection(event.element)
        else:
            self.updateStatusBar(event.name)
            if isinstance(event, RotaryEvent):
                self.handle_rotary_event(event)
            if isinstance(event, ButtonEvent):
                self.handle_button(event.element)

    def handle_connection(self, device: hid.device):
        self.updateStatusBar(f"Connected to {device.get_manufacturer_string()} {device.get_product_string()}")

    def handle_rotary_event(self, rotary_event: RotaryEvent) -> None:
        if type(rotary_event.element) is Wheel:
            self.handle_wheel(rotary_event.element, rotary_event.direction, rotary_event.value)
        elif type(rotary_event.element) is Dial:
            self.handle_dial(rotary_event.element, rotary_event.direction, rotary_event.value)

    def handle_wheel(self, wheel: Wheel, direction: bool, value: int) -> None:
        self.WHEEL_MAP[wheel.pos].setChecked(True)

    def handle_dial(self, dial: Dial, direction: bool, value: int) -> None:
        self.dial.setValue(dial.pos)

    def handle_button(self, button: Button) -> None:
        self.BUTTON_MAP[button.num].setChecked(button.push)

    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        self.shuttle_worker.stop()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec())
