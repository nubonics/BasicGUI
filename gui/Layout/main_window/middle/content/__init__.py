from PySide6.QtWidgets import QWidget, QHBoxLayout


class Content(QWidget):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        widget.setStyleSheet(
            """
            background-color: blue;
            """
        )

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)
        hbox.addWidget(widget)

        self.setLayout(hbox)

