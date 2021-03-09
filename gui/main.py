# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import QRunnable, Slot, QThreadPool
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

import device.main
from gui_ui import Ui_GUI


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        # self.load_ui()  # Broken
        # Use pyside-uic form.ui > gui.py to generate the UI instead
        self.ui = Ui_GUI()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('images/icon.png'))
        self.ui.statusbar.showMessage("UI loaded!")

        self.threadpool = QThreadPool()
        worker = Worker()
        self.ui.statusbar.showMessage("Connecting...")
        self.threadpool.start(worker)

    # def load_ui(self):
    #     loader = QUiLoader()
    #     path = os.path.join(os.path.dirname(__file__), "gui.ui")
    #     ui_file = QFile(path)
    #     ui_file.open(QFile.ReadOnly)
    #     loader.load(ui_file, self)
    #     ui_file.close()


class Worker(QRunnable):
    @Slot()
    def run(self):
        device.main.connect(device.main.find_shuttle_device())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())
