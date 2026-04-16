import sys

from PyQt6.QtWidgets import QApplication
from window import Window
from utils.resource_utils import resource_path

app = QApplication(sys.argv)

window = Window()
window.show()

with open(resource_path("style.qss"), "r") as f:
    _style = f.read()
    window.setStyleSheet(_style)

app.exec()