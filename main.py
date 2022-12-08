import sys
import class_histogram as his
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QMainWindow, QComboBox, QPushButton, QLabel, QLineEdit, QHBoxLayout,
                             QVBoxLayout, QWidget, QDesktopWidget, QApplication, QMessageBox, QGridLayout, QMenu,
                             QDialog)

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import AddWindowDialog as AWinD


def create_menu(d, menu):
    if isinstance(d, list):
        for e in d:
            create_menu(e, menu)
    elif isinstance(d, dict):
        for k, v in d.items():
            sub_menu = QMenu(k, menu)
            menu.addMenu(sub_menu)
            create_menu(v, sub_menu)
    else:
        action = menu.addAction(d)
        action.setIconVisibleInMenu(False)


class AddWindow(QDialog):
    def __init__(self, parent=None):
        super(AddWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        validator = QIntValidator(100, 999)
        lable_0 = QLabel("Укажите значаение (μ): ")
        self.line_edit_0 = QLineEdit()
        self.line_edit_0.setValidator(validator)
        first_horizontal_box = QHBoxLayout()
        first_horizontal_box.addWidget(lable_0)
        first_horizontal_box.addWidget(self.line_edit_0)
        first_horizontal_box.addStretch()
        widget_layout = QWidget()
        widget_layout.setLayout(first_horizontal_box)
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


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.index = None
        self.plot = his.Ploter()
        self.initUI()

    def initUI(self):
        validator = QIntValidator(100, 999)
        # combo_box = QComboBox()
        # combo_box.addItems(["...", "Распределение разности средних", "Ошибка первого рода"])
        # combo_box.activated.connect(self.activated)
        button = QPushButton("Вычислить")
        button.clicked.connect(self.button)
        label1 = QLabel("Среднее значение (μ)")
        self.line_edit1 = QLineEdit("385")
        self.line_edit1.setValidator(validator)
        toolbar = NavigationToolbar(self.plot)
        label_0 = QLabel("Определите массив A:")
        label_1 = QLabel("Определите массив B:")
        label_2 = QLabel("Тип распределения А: ")
        label_3 = QLabel("Тип распределения B: ")
        grid = QGridLayout()
        # h_box_1 = QHBoxLayout()
        grid.addWidget(label_0, 0, 0)
        grid.addWidget(label_1, 0, 1)
        self.combo_box_0 = QComboBox()
        self.combo_box_0.addItems(["Массив A", "Нормальное распределение", "Распределение Вейбулла", "Гамма "
                                                                                                     "распределение"])
        self.combo_box_0.activated.connect(self.combo_box_activated)
        self.combo_box_1 = QComboBox()
        self.combo_box_1.addItems(["Массив B", "Нормальное распределение", "Распределение Вейбулла", "Гамма "
                                                                                                     "распределение"])
        self.combo_box_1.activated.connect(self.combo_box_activated)
        self.menu_0 = QMenu(self)
        create_menu(["Разность средних", {"Разность квантилей": ["10%", "20%", "30%"]}], self.menu_0)
        self.menu_0.triggered.connect(lambda action: button_2.setText(
            "Разность квантилей c " + action.text() if action.text() != "Разность средних" else "Разность средних"))
        button_2 = QPushButton("Метрика")
        button_2.setMenu(self.menu_0)
        self.menu_1 = QMenu(self)
        create_menu([{"Вероятность ошибки первого рода": ["1%", "5%", "10%"]}], self.menu_1)
        self.menu_1.triggered.connect(
            lambda action: button_3.setText("Вероятность ошибки первого рода c " + action.text()))
        button_3 = QPushButton("Вероятность ошибки первого рода")
        button_3.setMenu(self.menu_1)
        grid.addWidget(self.combo_box_0, 1, 0)
        grid.addWidget(self.combo_box_1, 1, 1)
        grid.addWidget(button_2, 1, 2)
        grid.addWidget(button_3, 1, 3)

        h_box_2 = QHBoxLayout()
        h_box_2.addStretch()
        h_box_2.addWidget(label1)
        h_box_2.addWidget(self.line_edit1)
        h_box_2.addStretch()

        h_box_3 = QHBoxLayout()
        h_box_3.addWidget(label_2)
        h_box_3.addWidget(label_3)
        h_box_3.addStretch()

        h3box = QHBoxLayout()
        h3box.addStretch()
        h3box.addWidget(button)
        h3box.addStretch()

        vbox = QVBoxLayout()
        vbox.addWidget(toolbar)
        vbox.addLayout(grid)
        vbox.addLayout(h_box_3)
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

    def combo_box_activated(self, index):
        if index == 1:
            self.dialog = AWinD.AddWindowDialog(index, self)
            self.dialog.show()
            self.dialog.button.clicked.connect(self.normal_array_generator)
        elif index == 2:
            self.dialog = AWinD.AddWindowDialog(index, self)
            self.dialog.show()
            self.dialog.button.clicked.connect(self.weibull_array_generator)
        elif index == 3:
            self.dialog = AWinD.AddWindowDialog(index, self)
            self.dialog.show()
            self.dialog.button.clicked.connect(self.gamma_array_generator)
        self.combo_box_0.setCurrentIndex(0)
        self.combo_box_1.setCurrentIndex(0)

    def normal_array_generator(self):
        print(his.normal_array_generator(float(self.dialog.line_edit_0.text().replace(',', '.')),
                                         float(self.dialog.line_edit_1.text().replace(',', '.'))))
        self.dialog.close()

    def weibull_array_generator(self):
        print(his.weibull_array_generator(float(self.dialog.line_edit_0.text().replace(',', '.'))))
        self.dialog.close()

    def gamma_array_generator(self):
        print(his.gamma_array_generator(float(self.dialog.line_edit_0.text().replace(',', '.')),
                                        float(self.dialog.line_edit_1.text().replace(',', '.'))))
        self.dialog.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
