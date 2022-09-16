import sys

from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QApplication, QMainWindow

from gui import *


class App(QMainWindow, Draggable):
    def __init__(self):
        super().__init__()

        width = int(config.get('window_size', 'width'))
        height = int(config.get('window_size', 'height'))

        self.resize(width, height)

        del width, height

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        main_widget = QWidget()
        main_widget.setLayout(Layout().gui_layout)
        main_widget.setContentsMargins(0, 0, 0, 0)

        self.setCentralWidget(main_widget)

        self.center_the_app()

        del main_widget

    def center_the_app(self):
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        del center
        self.move(geo.topLeft())
        del geo


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = App()
    window.show()

    app.exec()
