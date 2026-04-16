from PyQt6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt6.QtGui import QPixmap, QPainter, QColor, QBrush
from PyQt6.QtCore import Qt

class ProfileWidget(QLabel):
    def __init__(self, path: str):
        super().__init__()


        pixmap = QPixmap(path)
        radius = 8

        rounded = QPixmap(pixmap.size())
        rounded.fill(QColor("transparent"))

        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(pixmap))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(pixmap.rect(), radius, radius)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(12)
        shadow.setXOffset(4)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 63))

        self.setPixmap(rounded.scaled(64, 64, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.setObjectName("profile-picture")
        self.setGraphicsEffect(shadow)