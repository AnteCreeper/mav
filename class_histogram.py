# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 09:51:40 2021

@author: Mavrin S.V.

Для домашнего выполнения лаб. работ необходимо:
    1. Установить пакет Anaconda: https://repo.anaconda.com/archive/Anaconda3-2022.05-Windows-x86_64.exe
    2. После установки запустить Spyder
    3. Открыть этот файл и выполнить программу.


"""
# библиотеки
# from matplotlib.backends.backend_qt5agg import FigureCanvas
# from matplotlib.figure import Figure
import numpy as np
import scipy.stats as st
from sklearn.utils import resample
from sklearn.neighbors import KernelDensity  # используем класс из sklearn
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import random

def max_min(a, b, mu=0):
    min_b = min(a)
    min_a = min(b)
    max_b = max(b)
    max_a = max(a)
    if mu == 0:
        if max_b < max_a:
            if min_b < min_a:
                return max_a * 1.0001, min_b * 0.999
            else:
                return max_a * 1.0001, min_a * 0.999
        else:
            if min_b < min_a:
                return max_b * 1.0001, min_b * 0.999
            else:
                return max_b * 1.0001, min_a * 0.999
    else:
        dia = mu / 15
        if max_b < max_a:
            if min_b < min_a:
                return max_a + dia, min_b - dia
            else:
                return max_a + dia, min_a - dia
        else:
            if min_b < min_a:
                return max_b + dia, min_b - dia
            else:
                return max_b + dia, min_a - dia


class Solver():
    def __init__(self, list_A: np = None, list_B: np = None, mu=None, SKO=None, n_size_bootstrep=1000):
        if (list_A is None) or (list_B is None):
            start_random_seed = 999
            np.random.seed(start_random_seed)
        if mu is None:
            mu = 382
        persent = 1.002
        if SKO is None:
            SKO = 0.006 * mu
        if list_A is None:
            self.n_size_A = 180
            self.A = np.zeros([self.n_size_A])
            self.A = np.random.normal(mu, SKO, self.n_size_A)
        if list_B is None:
            self.n_size_B = 30
            self.B = np.zeros([self.n_size_B])
            self.B = np.random.normal(persent * mu, SKO, self.n_size_B)
        if list_A is not None:
            self.A = list_A
        if list_B is not None:
            self.B = list_B
        self.n_size_bootstrep = n_size_bootstrep

    def get_mean(self):
        return np.mean(self.B[:]) - np.mean(self.A[:])

    def get_bootstrep(self):
        delta = np.zeros([self.n_size_bootstrep])
        average_value_bootstrep_before = np.zeros([self.n_size_bootstrep])
        average_value_bootstrep_after = np.zeros([self.n_size_bootstrep])
        for i in range(self.n_size_bootstrep):
            boot = resample(self.A,
                            replace=True,
                            n_samples=self.n_size_A
                            )
            average_value_bootstrep_before[i] = np.mean(boot[:])
            boot = resample(self.B,
                            replace=True,
                            n_samples=self.n_size_B
                            )
            average_value_bootstrep_after[i] = np.mean(boot[:])
            delta[i] = np.mean(average_value_bootstrep_after) - np.mean(average_value_bootstrep_before)
        return delta

    def get_bootstrep_with_replace(self, n_size_Effect=1000):
        effect = np.zeros([n_size_Effect])
        # A_i = np.zeros([self.n_size_A])  # Объявляем массив
        # B_i = np.zeros([self.n_size_B])  # Объявляем массив
        for i in range(n_size_Effect):
            A_i = resample(self.A, replace=True)
            B_i = resample(self.B, replace=True)
            effect[i] = 100 * (np.mean(B_i) - np.mean(A_i[:])) / np.mean(A_i[:])
        return effect

    def get_delta_critich(self, delta):
        Alfa = 0.1
        return np.percentile(delta, 100 - Alfa * 100)
class Ploter(FigureCanvas):
    def __init__(self):
        """Инициализация

        Создаётся:
            name: имя переменной,
            distr: массив данных,
            fig,
            ax,
            prop
        """
        super(Ploter, self).__init__()
        # self.fig, self.ax = plt.subplots(figsize=(12, 4))
        self.prop = dict(  # Параметры Отрисовки Гистограммы
            alpha=1.0,  # Прозрачность
            linewidth=2,  # Толщина линии Прямоугольников
            linestyle='-',  # Стиль Линии
            edgecolor='black',  # Цвет Линии
            facecolor='skyblue')
        self.ax = self.figure.add_subplot()

    def plot_hist(self, distr, bins, label):
        """
        Рисует гистограмму

        distr : массив данных.
        bins : кол-во колбочек на гистограмме.
        max_y : максимальная высота в зависимости от инициализируемой сейчас гистограммы 
        """
        self.distr = distr
        self.middle = np.mean(self.distr[:])
        set = self.ax.hist(self.distr,
                           bins,
                           label=label,
                           density=True,
                           **self.prop)
        self.max_y = set[0].max() * 1.5
        self.ax.legend(loc="upper right", fontsize=12)

    def set_lim(self, left=None, right=None):
        """Задаёт приделы графика"""
        if (left is None) and (right is None):
            radius = ((max(self.distr) - self.middle) + (self.middle - min(self.distr))) / 2
            left = self.middle - radius * 1.3
            right = self.middle + radius * 1.3
        if left is None:
            left = min(self.distr) * 1.3 - self.middle * 0.3
        if right is None:
            right = max(self.distr) * 1.3 - self.middle * 0.3
        self.right_lim = right
        self.left_lim = left
        self.length = right - left
        self.ax.set_ylim(0, self.max_y)
        self.ax.set_xlim(self.left_lim, self.right_lim)

    def plot_kde(self, kde_parametrs, steps: int = 1000, color: str = 'navy'):
        """
        Рисуется огибающая и объявляются переменные

        Parameters
        ----------
        kde_parametrs : кривизна огибающей.
        steps : количество точек по которой строится кривая.
        color: свет линии
        """
        self.colorline = color
        kde_linespace = np.zeros([1, 2])
        kde_linespace[0, :] = [self.left_lim, self.right_lim]
        self.x = np.linspace(*kde_linespace[0, :], steps)
        self.kde = KernelDensity(bandwidth=kde_parametrs)
        self.kde.fit(self.distr[:, None])
        self.logprobes = self.kde.score_samples(self.x[:, None])
        self.ax.plot(self.x, np.exp(self.logprobes), lw=4, c=self.colorline)

    def plot_middle(self):
        """Рисует прямую описывающую середину гистограммы"""
        self.plot_line(self.middle, colors=self.colorline, linewidth=3, linestyles="--")

    def _fill_between(self, mean, bool_left: bool = False, color: str = 'darkred'):
        """Закрытый; закрашивает часть под кривой, и меняет цвет части этой прямой"""
        kde_linespace = np.zeros([1, 2])
        if not bool_left:
            kde_linespace[0, :] = [mean, self.right_lim]
            size = 200
            x_tex = self.right_lim - self.length * 0.1
        else:
            kde_linespace[0, :] = [self.left_lim, mean]
            size = 800
            x_tex = self.left_lim + self.length * 0.1
        _x = np.linspace(*kde_linespace[0, :], 1000)
        logprobes = self.kde.score_samples(_x[:, None])
        self.ax.plot(_x, np.exp(logprobes), lw=4, c=color)
        self.ax.fill_between(_x, np.exp(logprobes), color=color, alpha=0.3)
        self._plot_line_and_signature(mean, x_tex, self.max_y * 0.6, _x[size], np.exp(logprobes)[size])

    def plot_line(self, x_coor, linestyles: str = "-", colors: str = "k", linewidth=2):
        """Рисует вертикальную прямую"""
        self.ax.vlines(x_coor,  # координата по "x"
                       0, self.max_y,  # Начало и Конец пр "Y"
                       colors=colors,  # Цвет Линии
                       linewidth=linewidth,  # Толщина линии
                       linestyles=linestyles)  # Стиль Линии

    def plot_p_level(self, mean):
        """Рисует p-level"""
        self.plot_line(mean, "--", "darkred", 3)
        self._fill_between(mean)

    def set_facecolor(self, color='floralwhite'):
        """Добавляет цвет фона и фон сетки"""
        self.ax.set_facecolor(color)
        self.ax.grid(True, ls='--', linewidth=0.3, c='k', alpha=0.3)

    def title(self, title):
        """Задаёт название графика"""
        self.ax.set_title(title, fontsize=16)  # # Подпись над рисунком

    def _find_p_level(self, mean):
        """Вычисление p level"""
        print(mean, "=======")
        d = (100 - st.percentileofscore(self.distr, mean)) / 100
        dd = (100 - st.percentileofscore(self.distr, mean)) / 100
        print(d)
        print(dd)
        return dd

    def _plot_arrow(self, text, xtext, ytext, x, y, color='k'):
        """Вызов аннотации"""
        self.ax.annotate(text,
                         fontsize=14,
                         xy=(x, y),
                         xytext=(xtext, ytext),
                         arrowprops={'color': color, 'arrowstyle': '->', 'lw': 2}
                         )

    # сделать возможность автоматизировать
    def _plot_line_and_signature(self, mean, xtext, ytext, x, y):
        self._plot_arrow(f"{round(self._find_p_level(mean), 5)}", xtext, ytext,
                         x, y)

    def set_labels(self, xlabel, ylabel):
        """Подпись осей"""
        self.ax.set_xlabel(xlabel, fontsize=16)
        self.ax.set_ylabel(ylabel, fontsize=16)

    def plot_mistake_one_line(self, delta_critich):
        self.plot_line(delta_critich, colors='yellow', linewidth=4)
        self._fill_between(delta_critich, True, 'yellow')
        self._plot_indication_mistake(delta_critich)

    def _plot_indication_mistake(self, delta_critich):
        self._plot_arrow("Граница ошибки 1-го рода",
                         self.left_lim + self.length * 0.1,
                         self.max_y * 0.9,
                         delta_critich,
                         self.max_y * 0.7)

    def get_bootstrep_delta(self, a, b, bins, label, size=1000):
        """Создает бутстреп разности двух массивов, так же создает гистограмму методом plot_hist"""
        delta = np.zeros([size])
        result = np.concatenate([a, b])
        size_a = len(a)
        random_state = random.randint(1, 1000)
        for i in range(size):
            result = resample(result[:], replace=False, random_state=random_state)
            result_before, result_after = result[:size_a], result[size_a:]
            delta[i] = np.mean(result_before) - np.mean(result_after)
        self.plot_hist(delta, bins, label)

    def plot_bootstrep_effect(self, A, B, bins, label):
        n_size_Metrics_in_effect = 1000
        metrics_in_effect = np.zeros([n_size_Metrics_in_effect])

        # A_i = np.zeros([self.n_size_A])  # Объявляем массив
        # B_i = np.zeros([self.n_size_B])  # Объявляем массив
        random_state = random.randint(1, 1000)
        for i in range(n_size_Metrics_in_effect):

            A_i = resample(A, replace=True)
            B_i = resample(B, replace=True)

            metrics_in_effect[i] = np.mean(B_i) - np.mean(A_i[:])
        self.plot_hist(metrics_in_effect, bins, label)

    def plot(self):
        sol1 = Solver(mu=100, SKO=0.006)
        self.canvas.get_bootstrep_delta(sol1.A, sol1.B, 20, "Разность средних")
    def distribution_of_the_mean_difference(self, mu):
        """Распределение разности средних"""
        sol1 = Solver(mu=mu)
        self.get_bootstrep_delta(sol1.A, sol1.B, 20, "Разность средних")
        self.set_lim()
        self.plot_kde(0.08)
        self.plot_middle()
        self.plot_p_level(sol1.get_mean())
        print(sol1.get_mean(), "<<<<<===")
        self.set_facecolor()
        self.set_labels("Плотность вероятности", "Разность средних")
        self.title("Распределение разности средних от Histogram")
        self.draw()
        print()

    def mistake_one_line(self, mu):
        sol2 = Solver(mu=mu)
        self.plot_bootstrep_effect(sol2.A, sol2.B, 20, "Разность средних")
        self.set_lim()
        self.plot_kde(0.08)
        self.plot_middle()
        self.plot_mistake_one_line(sol2.get_delta_critich(sol2.get_bootstrep()))
        self.set_facecolor()
        self.set_labels("Плотность вероятности", "Разность средних")
        self.title("Ошибка первого рода от Histogram")
        self.draw()

# distribution_of_the_mean_difference(382, 0.006)
#mistake_one_line(382, 0.006)
#plt.show()
