from PySide6.QtWidgets import QVBoxLayout

from .main_window import *
from .custom_enhancements import *


class Layout(QWidget):
    def __init__(self):
        super().__init__()

        self.gui_layout = QVBoxLayout()
        self.gui_layout.addWidget(Top(), stretch=1)
        self.gui_layout.addLayout(Middle().middle_layout, stretch=15)
        self.gui_layout.addWidget(Bottom(), stretch=1)
        self.gui_layout.setSpacing(0)
