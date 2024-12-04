import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from PyQt6.QtCore import Qt, QRect
from PyQt6 import uic
import random


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.button = QPushButton("Добавить круг")
        self.button.clicked.connect(self.addCircle)
        self.layout.addWidget(self.button)
        self.show()

    def addCircle(self):
        x = random.randint(0, 700)
        y = random.randint(0, 500)
        diameter = random.randint(10, 100)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for x, y, diameter in self.circles:
            qp.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            qp.setBrush(QBrush(QColor(255, 255, 0)))
            qp.drawEllipse(QRect(x, y, diameter, diameter))
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())