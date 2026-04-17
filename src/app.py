import PyQt6.QtWidgets
import PyQt6.QtCore
import widgets.top_row_container

class App(PyQt6.QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

        layout = PyQt6.QtWidgets.QVBoxLayout()

        layout.addWidget(widgets.top_row_container.TopRowContainer(), alignment=PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)


        self.setLayout(layout)
        self.setObjectName("app")