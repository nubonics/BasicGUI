
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget


class Draggable(QWidget):
    """
    This class is to allow the main window to be resizable & draggable.
    """

    def __init__(self):
        super().__init__()
        self.oldPos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.oldPos is not None:
            delta = event.globalPos() - self.oldPos
            self.move(self.pos() + delta)
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.oldPos = None