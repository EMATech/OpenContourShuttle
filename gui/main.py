# This Python file uses the following encoding: utf-8

import sys

import PySide6
from PySide6.QtCore import QThread
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu

import device.main
from gui_ui import Ui_GUI


class Connection(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        conn = device.main.ShuttleXpressConnection(device.main.find_shuttle_devices()[0])  # TODO: Support multiple HIDs
        conn.connect()


class GUI(QMainWindow):
    connection = Connection()

    def __init__(self):
        super(GUI, self).__init__()
        self.icon = QIcon('images/icon.png')

        if QSystemTrayIcon.isSystemTrayAvailable():
            self.systray = QSystemTrayIcon()
            self.systray.setIcon(self.icon)
            systray_menu = QMenu(title="GUI", parent=self)
            quit_action = QAction("&Quit", self)
            systray_menu.addAction(quit_action)
            quit_action.triggered.connect(self.close)
            self.systray.setContextMenu(systray_menu)
            self.systray.setVisible(True)

        # self.load_ui()  # Broken
        # Use pyside-uic form.ui > gui.py to generate the UI instead
        self.ui = Ui_GUI()
        self.ui.setupUi(self)
        self.setWindowIcon(self.icon)
        self.updateStatusBar("UI loaded!")

        self.updateStatusBar("Connecting...")
        self.connection.start()
        self.updateStatusBar("Connected")

    # def load_ui(self):
    #     loader = QUiLoader()
    #     path = os.path.join(os.path.dirname(__file__), "gui.ui")
    #     ui_file = QFile(path)
    #     ui_file.open(QFile.ReadOnly)
    #     loader.load(ui_file, self)
    #     ui_file.close()

    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        # FIXME: properly stop the thread
        self.connection.terminate()

    def updateStatusBar(self, message):
        self.ui.statusbar.showMessage(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())
