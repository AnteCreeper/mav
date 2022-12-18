from PyQt5.QtWidgets import (QMainWindow, QComboBox, QPushButton, QLabel, QLineEdit, QHBoxLayout,
                             QVBoxLayout, QWidget, QDesktopWidget, QApplication, QMessageBox, QGridLayout, QMenu,
                             QDialog)
from PyQt5.QtGui import QIntValidator, QDoubleValidator


class AddWindowDialog(QDialog):
    def __init__(self, index, parent):
        super(AddWindowDialog, self).__init__(parent)
        self.double_validator = QDoubleValidator()
        self.int_validator = QIntValidator(1, 100000)

        label = QLabel("Укажите количество элементов: ")
        self.line_edit = QLineEdit()
        self.line_edit.setValidator(self.int_validator)
        self.zero_horizontal_box = QHBoxLayout()
        self.zero_horizontal_box.addWidget(label)
        self.zero_horizontal_box.addWidget(self.line_edit)
        self.zero_horizontal_box.addStretch()

        if index == 1:
            self.initUI_normal()
        elif index == 2:
            self.initUI_weibull()
        elif index == 3:
            self.initUI_gamma()

    def initUI_normal(self):

        label_0 = QLabel("Укажите значение центра μ: ")
        self.line_edit_0 = QLineEdit()
        self.line_edit_0.setValidator(self.double_validator)
        first_horizontal_box = QHBoxLayout()
        first_horizontal_box.addWidget(label_0)
        first_horizontal_box.addWidget(self.line_edit_0)
        first_horizontal_box.addStretch()

        label_1 = QLabel("Укажите стандартное отклонение σ: ")
        self.line_edit_1 = QLineEdit()
        self.line_edit_1.setValidator(self.double_validator)
        second_horizontal_box = QHBoxLayout()
        second_horizontal_box.addWidget(label_1)
        second_horizontal_box.addWidget(self.line_edit_1)
        second_horizontal_box.addStretch()

        # label_2 = QLabel("Укажите количество элементов массива: ")
        # self.line_edit_2 = QLineEdit()
        # self.line_edit_2.setValidator(self.double_validator)
        # third_horizontal_box = QHBoxLayout()
        # third_horizontal_box.addWidget(label_2)
        # third_horizontal_box.addWidget(self.line_edit_2)
        # third_horizontal_box.addStretch()

        self.button = QPushButton("Сгенерировать")
        vbox = QVBoxLayout()
        vbox.addLayout(self.zero_horizontal_box)
        vbox.addLayout(first_horizontal_box)
        vbox.addLayout(second_horizontal_box)
        # vbox.addLayout(third_horizontal_box)
        vbox.addWidget(self.button)

        widget_layout = QWidget(self)
        widget_layout.setLayout(vbox)
        self.initUI_end()

    def initUI_weibull(self):
        label_0 = QLabel("Укажите параметр формы a: ")
        self.line_edit_0 = QLineEdit()
        self.line_edit_0.setValidator(self.double_validator)
        first_horizontal_box = QHBoxLayout()
        first_horizontal_box.addWidget(label_0)
        first_horizontal_box.addWidget(self.line_edit_0)
        first_horizontal_box.addStretch()

        self.button = QPushButton("Сгенерировать")
        vbox = QVBoxLayout()
        vbox.addLayout(self.zero_horizontal_box)
        vbox.addLayout(first_horizontal_box)
        vbox.addWidget(self.button)

        widget_layout = QWidget(self)
        widget_layout.setLayout(vbox)
        self.initUI_end()

    def initUI_gamma(self):
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
        vbox.addLayout(self.zero_horizontal_box)
        vbox.addLayout(first_horizontal_box)
        vbox.addLayout(second_horizontal_box)
        vbox.addWidget(self.button)

        widget_layout = QWidget(self)
        widget_layout.setLayout(vbox)
        self.initUI_end()

    def initUI_end(self):
        self.setWindowTitle('Построить график')
        self.resize(650, 650)
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
