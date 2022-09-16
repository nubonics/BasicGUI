from PySide6.QtWidgets import QHBoxLayout

from .content import *
from .sidebar import *


class Middle(Sidebar, Content):
    def __init__(self):
        super().__init__()

        self.middle_layout = QHBoxLayout()
        self.middle_layout.setSpacing(0)
        self.middle_layout.addWidget(Sidebar(), stretch=1)
        self.middle_layout.addWidget(Content(), stretch=5)
