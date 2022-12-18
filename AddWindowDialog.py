from PyQt5.QtWidgets import (QMainWindow, QComboBox, QPushButton, QLabel, QLineEdit, QHBoxLayout,
                             QVBoxLayout, QWidget, QDesktopWidget, QApplication, QMessageBox, QGridLayout, QMenu,
                             QDialog)
from PyQt5.QtGui import QDoubleValidator
from PyQt5 import QtCore


class AddWindowDialog(QDialog):
    def __init__(self, index, parent):
        super(AddWindowDialog, self).__init__(parent)
        self.double_validator = QDoubleValidator()
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        if index == 1:
            self.initUI_normal()
        elif index == 2:
            self.initUI_weibull()
        elif index == 3:
            self.initUI_gamma()

    def initUI_normal(self):

        self.setFixedSize(490, 180)

        label_0 = QLabel("Укажите значение μ: ")
        self.line_edit_0 = QLineEdit()
        self.line_edit_0.setValidator(self.double_validator)
        first_horizontal_box = QHBoxLayout()
        first_horizontal_box.addWidget(label_0)
        first_horizontal_box.addWidget(self.line_edit_0)
        first_horizontal_box.addStretch()

        label_1 = QLabel("Укажите коэффициент для σ: ")
        self.line_edit_1 = QLineEdit()
        self.line_edit_1.setValidator(self.double_validator)
        second_horizontal_box = QHBoxLayout()
        second_horizontal_box.addWidget(label_1)
        second_horizontal_box.addWidget(self.line_edit_1)
        second_horizontal_box.addStretch()

        label_2 = QLabel("Укажите количество элементов массива: ")
        self.line_edit_2 = QLineEdit()
        self.line_edit_2.setValidator(self.double_validator)
        third_horizontal_box = QHBoxLayout()
        third_horizontal_box.addWidget(label_2)
        third_horizontal_box.addWidget(self.line_edit_2)
        third_horizontal_box.addStretch()

        self.button = QPushButton("Сгенерировать")
        vbox = QVBoxLayout()
        vbox.addLayout(first_horizontal_box)
        vbox.addLayout(second_horizontal_box)
        vbox.addLayout(third_horizontal_box)
        vbox.addWidget(self.button)

        widget_layout = QWidget(self)
        widget_layout.setLayout(vbox)
        self.initUI_end()

    def initUI_weibull(self):
        self.setFixedSize(350, 100)
        label_0 = QLabel("Укажите значение a: ")
        self.line_edit_0 = QLineEdit()
        self.line_edit_0.setValidator(self.double_validator)
        first_horizontal_box = QHBoxLayout()
        first_horizontal_box.addWidget(label_0)
        first_horizontal_box.addWidget(self.line_edit_0)
        first_horizontal_box.addStretch()

        self.button = QPushButton("Сгенерировать")
        vbox = QVBoxLayout()
        vbox.addLayout(first_horizontal_box)
        vbox.addWidget(self.button)

        widget_layout = QWidget(self)
        widget_layout.setLayout(vbox)
        self.initUI_end()

    def initUI_gamma(self):
        self.setFixedSize(430, 140)
        label_0 = QLabel("Укажите параметр формы λ: ")
        self.line_edit_0 = QLineEdit()
        self.line_edit_0.setValidator(self.double_validator)
        first_horizontal_box = QHBoxLayout()
        first_horizontal_box.addWidget(label_0)
        first_horizontal_box.addWidget(self.line_edit_0)
        first_horizontal_box.addStretch()

        label_1 = QLabel("Укажите параметр масштаба α: ")
        self.line_edit_1 = QLineEdit()
        self.line_edit_1.setValidator(self.double_validator)
        second_horizontal_box = QHBoxLayout()
        second_horizontal_box.addWidget(label_1)
        second_horizontal_box.addWidget(self.line_edit_1)
        second_horizontal_box.addStretch()

        self.button = QPushButton("Сгенерировать")
        vbox = QVBoxLayout()
        vbox.addLayout(first_horizontal_box)
        vbox.addLayout(second_horizontal_box)
        vbox.addWidget(self.button)

        widget_layout = QWidget(self)
        widget_layout.setLayout(vbox)
        self.initUI_end()

    def initUI_end(self):
        self.setWindowTitle('Построить график')
        self.center()
        self.show()

    def center(self):
        """Функция центрирования"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # def button(self):
    #     pass
