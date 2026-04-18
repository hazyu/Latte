import PyQt6.QtWidgets
import PyQt6.QtCore
import containers.top_row_container
import containers.middle_row_container

class App(PyQt6.QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

        layout = PyQt6.QtWidgets.QVBoxLayout()

        layout.addWidget(containers.top_row_container.TopRowContainer(), alignment=PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(containers.middle_row_container.MiddleRowContainer(), alignment=PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
        self.setContentsMargins(0, 0, 0, 0)
        self.setObjectName("app")