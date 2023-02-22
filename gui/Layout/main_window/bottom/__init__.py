from PySide6.QtWidgets import QWidget, QHBoxLayout


class Bottom(QWidget):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        widget.setStyleSheet(
            """
            background-color: #343434;
            border-bottom-left-radius : 10px;
            border-bottom-right-radius : 10px;
            """
        )

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)
        hbox.addWidget(widget)

        self.setLayout(hbox)