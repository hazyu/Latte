from PyQt6.QtWidgets import QFrame, QVBoxLayout
from ui.widgets.profile_widget import ProfileWidget
from utils.resource_utils import resource_path

class HomeContainer(QFrame):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.setObjectName("widget")
        self.setLayout(layout)

        layout.addWidget(ProfileWidget(resource_path("profile.jpg")))

