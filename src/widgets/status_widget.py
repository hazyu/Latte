import PyQt6.QtWidgets
import widgets.speaker_widget

class StatusWidget(PyQt6.QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

        layout = PyQt6.QtWidgets.QHBoxLayout()
        layout.addWidget(widgets.speaker_widget.SpeakerWidget())

        self.setFixedSize(198, 50)
        self.setLayout(layout)
        self.setObjectName("status-widget")

