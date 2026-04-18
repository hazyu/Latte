import PyQt6.QtWidgets
import PyQt6.QtCore
import widgets.navigation_widget

class MiddleRowContainer(PyQt6.QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

        layout = PyQt6.QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(widgets.navigation_widget.NavigationWidget(), alignment=PyQt6.QtCore.Qt.AlignmentFlag.AlignLeft)

        self.setObjectName("middle-row-container")
        self.setLayout(layout)
        self.setFixedSize(1216, 500)