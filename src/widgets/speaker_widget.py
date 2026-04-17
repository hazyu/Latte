from PyQt6.QtGui import QKeyEvent
import PyQt6.QtWidgets
import PyQt6.QtCore
import PyQt6.QtSvgWidgets
import utils.resource_utils

class SpeakerWidget(PyQt6.QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()

        speaker_icon = PyQt6.QtSvgWidgets.QGraphicsSvgItem(utils.resource_utils.get_resource_path("speaker.svg"))
        speaker_icon.setPos(-(18 + 13) + 4.5, 0)
        
        self.small_wave_icon = PyQt6.QtSvgWidgets.QGraphicsSvgItem(utils.resource_utils.get_resource_path("speaker_small_wave.svg"))
        self.small_wave_icon.setPos(-9, 6.5)
        
        self.large_wave_icon = PyQt6.QtSvgWidgets.QGraphicsSvgItem(utils.resource_utils.get_resource_path("speaker_large_wave.svg"))
        self.large_wave_icon.setPos(-(4.5 + 6) + 8.5, 3.5)

        scene = PyQt6.QtWidgets.QGraphicsScene(self)
        scene.addItem(speaker_icon)
        scene.addItem(self.small_wave_icon)
        scene.addItem(self.large_wave_icon)

        self.setScene(scene)
        self.setFixedSize(36, 36)
        self.setObjectName("speaker")

        self.volume = 100

    def keyPressEvent(self, event: QKeyEvent | None):
        if event != None:
            if event.key() == PyQt6.QtCore.Qt.Key.Key_Down:
                if self.volume > 0:
                    self.volume -= 5

                if self.volume < 50:
                    self.large_wave_icon.hide()

                if self.volume == 0:
                    self.small_wave_icon.hide()
            elif event.key() == PyQt6.QtCore.Qt.Key.Key_Up:
                if self.volume < 100:
                    self.volume += 5

                if self.volume > 0:
                    self.small_wave_icon.show()

                if self.volume > 50:
                    self.large_wave_icon.show()
                    

        
        super().keyPressEvent(event)