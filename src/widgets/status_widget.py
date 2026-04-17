import PyQt6.QtWidgets
import PyQt6.QtCore
import widgets.speaker_widget
import widgets.time_widget

class StatusWidget(PyQt6.QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

        layout = PyQt6.QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(widgets.speaker_widget.SpeakerWidget(), alignment=PyQt6.QtCore.Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(widgets.time_widget.TimeWidget(), alignment=PyQt6.QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.setFixedSize(198, 50)
        self.setLayout(layout)
        self.setObjectName("status-widget")

