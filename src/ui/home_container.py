from PyQt6.QtWidgets import QFrame, QVBoxLayout

class HomeContainer(QFrame):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.setObjectName("widget")
        self.setLayout(layout)

