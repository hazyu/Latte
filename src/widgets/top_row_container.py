import PyQt6.QtWidgets
import widgets.profile_widget
import widgets.status_widget

class TopRowContainer(PyQt6.QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

        layout = PyQt6.QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(widgets.profile_widget.ProfileWidget())
        layout.addWidget(widgets.status_widget.StatusWidget())
        

        self.setObjectName("top-row-container")
        self.setLayout(layout)
        self.setFixedSize(1210, 64)