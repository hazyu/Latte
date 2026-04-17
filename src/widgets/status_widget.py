import PyQt6.QtWidgets
import PyQt6.QtCore
import widgets.speaker_widget
import widgets.time_widget
import widgets.battery_widget

class StatusWidget(PyQt6.QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

        layout = PyQt6.QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 13, 0)
        layout.setSpacing(5)
        layout.addWidget(widgets.speaker_widget.SpeakerWidget(), alignment=PyQt6.QtCore.Qt.AlignmentFlag.AlignVCenter | PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(widgets.battery_widget.BatteryWidget(), alignment=PyQt6.QtCore.Qt.AlignmentFlag.AlignVCenter | PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(widgets.time_widget.TimeWidget(), alignment=PyQt6.QtCore.Qt.AlignmentFlag.AlignVCenter | PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)

        self.setFixedSize(198, 50)
        self.setLayout(layout)
        self.setObjectName("status-widget")

