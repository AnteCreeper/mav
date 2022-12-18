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


# class AddWindow(QDialog):
#     def __init__(self, parent=None):
#         super(AddWindow, self).__init__(parent)
#
#         self.initUI()
#
#     def initUI(self):
#         validator = QIntValidator(100, 999)
#         lable_0 = QLabel("Укажите значаение (μ): ")
#         self.line_edit_0 = QLineEdit()
#         self.line_edit_0.setValidator(validator)
#         first_horizontal_box = QHBoxLayout()
#         first_horizontal_box.addWidget(lable_0)
#         first_horizontal_box.addWidget(self.line_edit_0)
#         first_horizontal_box.addStretch()
#         widget_layout = QWidget()
#         widget_layout.setLayout(first_horizontal_box)
#         self.setWindowTitle('Построить график')
#         self.resize(650, 650)
#         self.center()
#         self.show()
#
#     def center(self):
#         """Функция центрирования"""
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.index = None
        self.current_text_0 = "Массив A"
        self.current_text_1 = "Массив B"
        self.A_array = None
        self.B_array = None
        self.combo_current_0 = False
        self.combo_current_1 = False

        self.plot = his.Ploter()
        self.initUI()

    def initUI(self):
        # validator = QIntValidator(100, 999)
        # combo_box = QComboBox()
        # combo_box.addItems(["...", "Распределение разности средних", "Ошибка первого рода"])
        # combo_box.activated.connect(self.activated)
        # button = QPushButton("Вычислить")
        # button.clicked.connect(self.button)
        # label1 = QLabel("Среднее значение (μ)")
        # self.line_edit1 = QLineEdit("385")
        # self.line_edit1.setValidator(validator)
        toolbar = NavigationToolbar(self.plot)
        label_0 = QLabel("Определите массив A:")
        label_1 = QLabel("Определите массив B:")
        self.label_2 = QLabel(" ")
        self.label_3 = QLabel(" ")
        grid = QGridLayout()
        # h_box_1 = QHBoxLayout()
        grid.addWidget(label_0, 0, 0)
        grid.addWidget(label_1, 0, 1)
        self.list_0 = ["Массив A", "Нормальное распределение", "Распределение Вейбулла", "Гамма распределение"]
        self.combo_box_0 = QComboBox()
        self.combo_box_0.addItems(self.list_0)
        self.combo_box_0.activated.connect(self.combo_box_activated_0)
        self.combo_box_1 = QComboBox()
        self.combo_box_1.addItems(["Массив B", "Нормальное распределение", "Распределение Вейбулла", "Гамма "
                                                                                                     "распределение"])
        self.combo_box_1.activated.connect(self.combo_box_activated_1)
        self.menu_0 = QMenu(self)
        create_menu(["Разность средних", {"Разность квантилей": ["10%", "20%", "30%"]}], self.menu_0)
        self.menu_0.triggered.connect(lambda action: button_2.setText(
            "Разность квантилей c " + action.text() if action.text() != "Разность средних" else "Разность средних"))
        self.menu_0.triggered.connect(lambda action: self.activate(action.text()))
        button_2 = QPushButton("Метрика")
        button_2.setMenu(self.menu_0)
        self.menu_1 = QMenu(self)
        create_menu([{"Вероятность ошибки первого рода": ["1%", "5%", "10%"]}], self.menu_1)
        self.menu_1.triggered.connect(
            lambda action: button_3.setText("Вероятность ошибки первого рода c " + action.text()))
        self.menu_1.triggered.connect(lambda action: self.activate(action.text()))
        button_3 = QPushButton("Вероятность ошибки первого рода")
        button_3.setMenu(self.menu_1)
        grid.addWidget(self.combo_box_0, 1, 0)
        grid.addWidget(self.combo_box_1, 1, 1)
        grid.addWidget(button_2, 1, 2)
        grid.addWidget(button_3, 1, 3)

        # h_box_2 = QHBoxLayout()
        # h_box_2.addStretch()
        # h_box_2.addWidget(label1)
        # h_box_2.addWidget(self.line_edit1)
        # h_box_2.addStretch()

        h_box_3 = QHBoxLayout()
        h_box_3.addWidget(self.label_2)
        h_box_3.addWidget(self.label_3)
        self.label_4_1 = QLabel(" ")
        self.label_4_2 = QLabel(" ")
        h_box_4 = QHBoxLayout()
        h_box_4.addWidget(self.label_4_1)
        h_box_4.addWidget(self.label_4_2)
        self.label_3_1 = QLabel(" ")
        self.label_3_2 = QLabel(" ")
        self.label_3_3 = QLabel(" ")
        self.label_3_4 = QLabel(" ")
        h_box_5 = QHBoxLayout()
        h_box_5.addWidget(self.label_3_1)
        h_box_5.addWidget(self.label_3_2)
        h_box_5.addWidget(self.label_3_3)
        h_box_5.addWidget(self.label_3_4)
        # h3box = QHBoxLayout()
        # h3box.addStretch()
        # h3box.addWidget(button)
        # h3box.addStretch()
        # insertItem
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(toolbar)
        self.vbox.addLayout(grid)
        self.vbox.addLayout(h_box_3)
        self.vbox.addLayout(h_box_4)
        self.vbox.addLayout(h_box_5)
        self.vbox.addWidget(self.plot)
        # self.vbox.addLayout(h3box)
        widget_layout = QWidget()
        widget_layout.setLayout(self.vbox)
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

    # def button(self):
    #     # if self.line_edit1.text() == "":
    #     #     QMessageBox.information(self, "Внимание!", "Введите среднее значение (μ)")
    #     # else:
    #     if self.index == 1:
    #         pass
    #         # self.plot.ax.clear()
    #         # self.plot.distribution_of_the_mean_difference(int(self.line_edit1.text()) + 0)
    #     if self.index == 2:
    #         pass
    #         # self.plot.ax.clear()
    #         # self.plot.mistake_one_line(int(self.line_edit1.text()) + 0)

    def combo_box_activated_0(self, index):
        self.combo_current_0 = True
        self.combo_box_activated(index)

    def combo_box_activated_1(self, index):
        self.combo_current_1 = True
        self.combo_box_activated(index)

    def combo_box_activated(self, index):
        if index == 1:
            self.dialog = AWinD.AddWindowDialog(index, self)
            self.dialog.show()
            self.dialog.button.clicked.connect(self.normal_array_generator)
        elif index == 2:
            self.dialog = AWinD.AddWindowDialog(index, self)
            print("111")
            self.dialog.show()
            self.dialog.button.clicked.connect(self.weibull_array_generator)
        elif index == 3:
            self.dialog = AWinD.AddWindowDialog(index, self)
            self.dialog.show()
            self.dialog.button.clicked.connect(self.gamma_array_generator)

    def add(self):
        h_box = QHBoxLayout()
        h_box.addWidget(self.label_2)
        h_box.addWidget(self.label_3)
        self.vbox.insertLayout(2, h_box)
        print("\n0", self.combo_current_0)
        print("1", self.combo_current_1)
        if self.combo_current_0:
            self.label_2.setText("Тип распределения A: " + self.combo_box_0.currentText())
            self.label_4_1.setText("Количество элементов: " + self.dialog.line_edit.text())
            self.combo_current_0 = False
        if self.combo_current_1:
            self.label_3.setText("Тип распределения B: " + self.combo_box_1.currentText())
            self.label_4_2.setText("Количество элементов: " + self.dialog.line_edit.text())
            self.combo_current_1 = False

    def normal_array_generator(self):
        bool_dialog = False
        errors_list = []
        if self.dialog.line_edit.text() == "":
            errors_list.append(self.dialog.label.text()[:-2] + '!' + '\n')
            print("333")
            bool_dialog = True
        if self.dialog.line_edit_0.text() == "":
            errors_list.append(self.dialog.label_0.text()[:-2] + '!' + '\n')
            bool_dialog = True
        if self.dialog.line_edit_1.text() == "":
            errors_list.append(self.dialog.label_1.text()[:-2] + '!' + '\n')
            bool_dialog = True
        if bool_dialog:
            errors_str = "".join(errors_list)
            QMessageBox.information(self, 'Внимание', errors_str)
        else:
            if self.combo_current_0:
                self.A_array = his.normal_array_generator(float(self.dialog.line_edit_0.text().replace(',', '.')),
                                                          float(self.dialog.line_edit_1.text().replace(',', '.')),
                                                          int(self.dialog.line_edit.text()))
                print("here")
                self.label_3_1.setText("Центр μ: " + self.dialog.line_edit_0.text())
                self.label_3_2.setText("Стандартное отклонение σ: " + self.dialog.line_edit_1.text())
            if self.combo_current_1:
                self.B_array = his.normal_array_generator(float(self.dialog.line_edit_0.text().replace(',', '.')),
                                                          float(self.dialog.line_edit_1.text().replace(',', '.')),
                                                          int(self.dialog.line_edit.text()))
                self.label_3_3.setText("Центр μ: " + self.dialog.line_edit_0.text())
                self.label_3_4.setText("Стандартное отклонение σ: " + self.dialog.line_edit_1.text())
            self.add()
            self.dialog.close()

    def weibull_array_generator(self):
        errors_list = []
        bool_dialog = False
        if self.dialog.line_edit.text() == "":
            errors_list.append(self.dialog.label.text()[:-2] + '!' + '\n')
            bool_dialog = True
        if self.dialog.line_edit_0.text() == "":
            errors_list.append(self.dialog.label_0.text()[:-2] + '!' + '\n')
            bool_dialog = True
        if bool_dialog:
            errors_str = "".join(errors_list)
            QMessageBox.information(self, 'Внимание', errors_str)
        else:
            if self.combo_current_0:
                print(self.combo_box_0.currentText())
                self.A_array = his.weibull_array_generator(float(self.dialog.line_edit_0.text().replace(',', '.')),
                                                           int(self.dialog.line_edit.text()))
                self.label_3_1.setText("Форма α: " + self.dialog.line_edit_0.text())
                self.label_3_2.setText(" ")
            if self.combo_current_1:
                print(self.combo_box_1.currentText())
                self.B_array = his.weibull_array_generator(float(self.dialog.line_edit_0.text().replace(',', '.')),
                                                           int(self.dialog.line_edit.text()))
                self.label_3_3.setText("Форма α: " + self.dialog.line_edit_0.text())
                self.label_3_4.setText(" ")
            self.add()
            self.dialog.close()

    def gamma_array_generator(self):

        errors_list = []
        bool_dialog = False
        if self.dialog.line_edit.text() == "":
            errors_list.append(self.dialog.label.text()[:-2] + '!' + '\n')
            bool_dialog = True
        if self.dialog.line_edit_0.text() == "":
            errors_list.append(self.dialog.label_0.text()[:-2] + '!' + '\n')
            bool_dialog = True
        if self.dialog.line_edit_1.text() == "":
            errors_list.append(self.dialog.label_1.text()[:-2] + '!' + '\n')
            bool_dialog = True
        if bool_dialog:
            errors_str = "".join(errors_list)
            QMessageBox.information(self, 'Внимание', errors_str)
        else:
            if self.combo_current_0:
                self.A_array = his.gamma_array_generator(float(self.dialog.line_edit_0.text().replace(',', '.')),
                                                         float(self.dialog.line_edit_1.text().replace(',', '.')),
                                                         int(self.dialog.line_edit.text()))
                self.label_3_1.setText("Форма λ: " + self.dialog.line_edit_0.text())
                self.label_3_2.setText("Масштаб α: " + self.dialog.line_edit_1.text())
            if self.combo_current_1:
                self.B_array = his.gamma_array_generator(float(self.dialog.line_edit_0.text().replace(',', '.')),
                                                         float(self.dialog.line_edit_1.text().replace(',', '.')),
                                                         int(self.dialog.line_edit.text()))
                self.label_3_3.setText("Форма λ: " + self.dialog.line_edit_0.text())
                self.label_3_4.setText("Масштаб α: " + self.dialog.line_edit_1.text())
            self.add()
            self.dialog.close()

    def activate(self, text):
        if self.A_array is None and self.B_array is None:
            message_box = QMessageBox()
            message_box.setWindowTitle("Внимание!")
            message_box.setText("Массивы А и В пустые!\nЗаполните их!")
            message_box.setIcon(QMessageBox.Warning)
            message_box.exec_()
        elif self.A_array is None:
            message_box = QMessageBox()
            message_box.setWindowTitle("Внимание!")
            message_box.setText("Массив А пуст!\nЗаполните его!")
            message_box.setIcon(QMessageBox.Warning)
            message_box.exec_()
        elif self.B_array is None:
            message_box = QMessageBox()
            message_box.setWindowTitle("Внимание!")
            message_box.setText("Массив B пуст!\nЗаполните его!")
            message_box.setIcon(QMessageBox.Warning)
            message_box.exec_()
        elif text == "Разность средних" or text == "10%" or text == "20%" or text == "30%":
            self.activate_0(text)
        elif text == "1%" or text == "5%" or text == "10%":
            self.activate_1(text)

    def activate_0(self, text):
        if text == "Разность средних":
            self.plot.ax.clear()
            self.plot.distribution_of_the_mean_difference(self.A_array, self.B_array)
            # self.plot.distribution_of_the_mean_difference(int(self.line_edit1.text()) + 0)
        elif text == "10%":
            self.plot.ax.clear()
            self.plot.quantile_difference(self.A_array, self.B_array, 10)
        elif text == "20%":
            self.plot.ax.clear()
            self.plot.quantile_difference(self.A_array, self.B_array, 20)
        elif text == "30%":
            self.plot.ax.clear()
            self.plot.quantile_difference(self.A_array, self.B_array, 30)

    def activate_1(self, text):
        if text == "1%":
            self.plot.ax.clear()
            self.plot.mistake_one_line(self.A_array, self.B_array, 0.01)
        elif text == "5%":
            self.plot.ax.clear()
            self.plot.mistake_one_line(self.A_array, self.B_array, 0.05)
        elif text == "10%":
            self.plot.ax.clear()
            self.plot.mistake_one_line(self.A_array, self.B_array, 0.1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
