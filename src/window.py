from PyQt6.QtWidgets import QMainWindow
from ui.home_container import HomeContainer

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(1280, 800)

        

        self.setCentralWidget(HomeContainer())
