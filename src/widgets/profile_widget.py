import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6.QtCore
import utils.resource_utils

class ProfileWidget(PyQt6.QtWidgets.QLabel):
    def __init__(self):
        super().__init__()

        pixmap = PyQt6.QtGui.QPixmap(utils.resource_utils.get_resource_path("profile.jpg"))
        scaled = pixmap.scaled(64, 64, PyQt6.QtCore.Qt.AspectRatioMode.KeepAspectRatio, PyQt6.QtCore.Qt.TransformationMode.SmoothTransformation)

        radius = 12

        #rounded pixmap
        rounded = PyQt6.QtGui.QPixmap(scaled.size())
        rounded.fill(PyQt6.QtGui.QColor("transparent"))

        painter = PyQt6.QtGui.QPainter(rounded)
        painter.setRenderHint(PyQt6.QtGui.QPainter.RenderHint.Antialiasing)
        painter.setBrush(PyQt6.QtGui.QBrush(scaled))
        painter.setPen(PyQt6.QtCore.Qt.PenStyle.NoPen)
        painter.drawRoundedRect(scaled.rect(), radius, radius)

        self.setPixmap(rounded)


        self.setObjectName("profile")