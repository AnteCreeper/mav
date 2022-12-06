import sys
import class_histogram as his
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QMainWindow, QComboBox, QPushButton, QLabel, QLineEdit, QHBoxLayout,
                             QVBoxLayout, QWidget, QDesktopWidget, QApplication, QMessageBox)

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.index = None
        self.plot = his.Ploter()
        self.initUI()

    def initUI(self):
        validator = QIntValidator(100, 999)
        combo_box = QComboBox()
        combo_box.addItems(["...", "Распределение разности средних", "Ошибка первого рода"])
        combo_box.activated.connect(self.activated)
        button = QPushButton("Вычислить")
        button.clicked.connect(self.button)
        label0 = QLabel("Выберите тип гистограммы: ")
        label1 = QLabel("Среднее значение (μ)")
        self.line_edit1 = QLineEdit("385")
        self.line_edit1.setValidator(validator)
        toolbar = NavigationToolbar(self.plot)
        h1box = QHBoxLayout()
        h1box.addStretch()
        h1box.addWidget(label0)
        h1box.addWidget(combo_box)
        h1box.addStretch()
        h2box = QHBoxLayout()
        h2box.addStretch()
        h2box.addWidget(label1)
        h2box.addWidget(self.line_edit1)
        h2box.addStretch()
        h3box = QHBoxLayout()
        h3box.addStretch()
        h3box.addWidget(button)
        h3box.addStretch()
        vbox = QVBoxLayout()
        vbox.addWidget(toolbar)
        vbox.addLayout(h1box)
        vbox.addLayout(h2box)
        vbox.addWidget(self.plot)
        vbox.addLayout(h3box)
        widget_layout = QWidget()
        widget_layout.setLayout(vbox)
        self.setCentralWidget(widget_layout)
        self.setWindowTitle('Построить график')
        self.resize(900, 650)
        self.center()
        self.show()

    def center(self):
        """Функция центрирования"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def button(self):
        if self.line_edit1.text() == "":
            QMessageBox.information(self, "Внимание!", "Введите среднее значение (μ)")
        else:
            if self.index == 1:
                self.plot.ax.clear()
                self.plot.distribution_of_the_mean_difference(int(self.line_edit1.text()) + 0)
            if self.index == 2:
                self.plot.ax.clear()
                self.plot.mistake_one_line(int(self.line_edit1.text()) + 0)

    def activated(self, index):
        self.index = index


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
