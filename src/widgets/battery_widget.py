import psutil
import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6.QtCore
import PyQt6.QtSvgWidgets
import utils.resource_utils

class BatteryWidget(PyQt6.QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()

        battery_top = PyQt6.QtSvgWidgets.QGraphicsSvgItem(utils.resource_utils.get_resource_path("battery_top.svg"))
        
        battery_outside = PyQt6.QtSvgWidgets.QGraphicsSvgItem(utils.resource_utils.get_resource_path("battery_outside.svg"))
        self.battery_inside = PyQt6.QtSvgWidgets.QGraphicsSvgItem(utils.resource_utils.get_resource_path("battery_inside.svg"))

        battery_top.setPos(2.25, -6)
        self.battery_inside.setPos(3, 2.75)

        self.bt_inside_fh = self.battery_inside.boundingRect().height()
        self.bt_inside_tr = PyQt6.QtGui.QTransform()

        self.battery = psutil.sensors_battery()
        if self.battery != None:
            self.percent = self.battery.percent
            scale = self.percent / 100
            self.set_battery_height(scale)
            
            
        self.timer = PyQt6.QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_battery)
        self.timer.start(5000)

        scene = PyQt6.QtWidgets.QGraphicsScene()
        scene.addItem(battery_top)
        scene.addItem(self.battery_inside)
        scene.addItem(battery_outside)

        self.setScene(scene)
        self.setFixedSize(36, 36)
        self.setObjectName("battery-widget")

    def set_battery_height(self, scale: float):
        self.bt_inside_tr = PyQt6.QtGui.QTransform()
        self.bt_inside_tr.translate(0, self.bt_inside_fh)
        self.bt_inside_tr.scale(1, scale)
        self.bt_inside_tr.translate(0, -self.bt_inside_fh)

        self.battery_inside.setTransform(self.bt_inside_tr)

    def update_battery(self):
        if self.battery != None:
            self.percent = self.battery.percent
            scale = self.percent / 100

            self.set_battery_height(scale)
