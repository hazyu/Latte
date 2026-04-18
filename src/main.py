from PyQt6.QtGui import QKeyEvent
import PyQt6.QtCore
import PyQt6.QtWidgets
import app
import sys
import utils.resource_utils
import utils.font_utils

class Window(PyQt6.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Latte")
        self.setFixedSize(1280, 800)
        self.setWindowFlag(PyQt6.QtCore.Qt.WindowType.FramelessWindowHint)

        self.setCentralWidget(app.App())

    def keyPressEvent(self, event: QKeyEvent): # type: ignore
        if event.key() == PyQt6.QtCore.Qt.Key.Key_Escape:
            self.close()

        
        super().keyPressEvent(event)

qt_app = PyQt6.QtWidgets.QApplication(sys.argv)

utils.font_utils.load_fonts()

window = Window()
window.show()

with open(utils.resource_utils.get_resource_path("style.qss"), "r") as f:
    _style = f.read()
    window.setStyleSheet(_style)

qt_app.exec()