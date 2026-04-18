from PyQt6.QtGui import QKeyEvent
import PyQt6.QtWidgets
import PyQt6.QtSvgWidgets
import PyQt6.QtCore
import utils.resource_utils

class NavigationWidget(PyQt6.QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

        layout = PyQt6.QtWidgets.QVBoxLayout()

        home_icon = PyQt6.QtSvgWidgets.QSvgWidget(utils.resource_utils.get_resource_path("home.svg"))
        home_icon.setFixedSize(48, 48)

        grid_icon = PyQt6.QtSvgWidgets.QSvgWidget(utils.resource_utils.get_resource_path("grid.svg"))
        grid_icon.setFixedSize(48, 48)

        images_icon = PyQt6.QtSvgWidgets.QSvgWidget(utils.resource_utils.get_resource_path("images.svg"))
        images_icon.setFixedSize(48, 48)

        music_icon = PyQt6.QtSvgWidgets.QSvgWidget(utils.resource_utils.get_resource_path("music.svg"))
        music_icon.setFixedSize(48, 48)

        settings_icon = PyQt6.QtSvgWidgets.QSvgWidget(utils.resource_utils.get_resource_path("settings.svg"))
        settings_icon.setFixedSize(48, 48)

        power_icon = PyQt6.QtSvgWidgets.QSvgWidget(utils.resource_utils.get_resource_path("power.svg"))
        power_icon.setFixedSize(48, 48)

        center = PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter

        layout.addWidget(home_icon, alignment=center)
        layout.addWidget(grid_icon, alignment=center)
        layout.addWidget(images_icon, alignment=center)
        layout.addWidget(music_icon, alignment=center)
        layout.addWidget(settings_icon, alignment=center)
        layout.addWidget(power_icon, alignment=center)

        self.setLayout(layout)
        self.setObjectName("navigation-widget")
        self.setFixedSize(75, 500)


        

