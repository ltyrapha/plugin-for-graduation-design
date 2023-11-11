from PyQt5.QtWidgets import QMessageBox
from qgis.PyQt import QtCore
from qgis._gui import QgsMapToolEmitPoint


class MapToolEmitPoint(QgsMapToolEmitPoint):
    # 自定义单击信号
    canvasSingleClicked = QtCore.pyqtSignal(object)

    def __init__(self, canvas):
        # self.iface = iface
        self.canvas = canvas
        self.mouseMoved = False
        self.mousePressed = False
        QgsMapToolEmitPoint.__init__(self, self.canvas)

    def canvasPressEvent(self, e):
        self.mousePressed = True

    def canvasMoveEvent(self, e):
        if self.mousePressed:
            self.mouseMoved = True

    def canvasReleaseEvent(self, e):
        # 如果鼠标是按下后拖动再松开，则不触发单击事件，若是按下后直接松开，则触发单击事件
        if not self.mouseMoved:
            self.mouseMoved = False
            self.mousePressed = False
            self.canvasSingleClicked.emit(e)
