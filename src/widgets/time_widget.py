import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6.QtCore
import utils.font_utils
import datetime

class TimeWidget(PyQt6.QtWidgets.QLabel):
    def __init__(self):
        super().__init__()

        self.timer = PyQt6.QtCore.QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        current_time = PyQt6.QtCore.QTime.currentTime().toString("hh:mm")

        self.setFont(PyQt6.QtGui.QFont(utils.font_utils.get_inter_font(), 32))
        self.setText(current_time)

    def show_time(self):
        current_time = PyQt6.QtCore.QTime.currentTime().toString("hh:mm")
        self.setText(current_time)