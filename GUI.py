from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Histogram")
        self.setGeometry(400, 300, 600, 400)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Histogram")
        self.main_text.move(200, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(200, 150)
        self.btn.setText("Изобразить")
        self.btn.setFixedWidth(200)
        self.btn.clicked(self.add_lable)


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()



    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
