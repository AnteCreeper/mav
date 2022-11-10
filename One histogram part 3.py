# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 09:51:40 2021

@author: Mavrin S.V.

Для домашнего выполнения лаб. работ необходимо:
    1. Установить пакет Anaconda: https://repo.anaconda.com/archive/Anaconda3-2022.05-Windows-x86_64.exe
    2. После установки запустить Spyder
    3. Открыть этот файл и выполнить программу.


"""
#библиотеки
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st



#import Bootstrep as bs


def max_min(a, b, mu = 0):
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
        dia = mu/15
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
        


        
    


#основа рондома
Start_random_seed = 990 #997  (0.015) 995 (0.029) 990(0.057)
np.random.seed(Start_random_seed)

#размеры выборок
n_size_A=180
n_size_B=30
n_size_Result=1000
n_size_Result_all = n_size_A + n_size_B

#интервалы и важные параметры
#m = np.random.randint(20, 1000)

mu1=382#50#
dia = mu1/15                                                                        #mu1=50
SKO1=0.006*mu1#0.008*mu1##*m#0.3#
persent = 1.002
A = np.zeros([n_size_A])
B = np.zeros([n_size_B])
Confidence_Interval=np.random.randint(85, 95)
Confidence_Interval=85  
Confidence_Interval_New=30
Left_border_Conf_Inter=(100-Confidence_Interval)/2
Right_border_Conf_Inter=Confidence_Interval + Left_border_Conf_Inter

#вывод важных параметров
print("mu1=",mu1,"  SKO1=",SKO1)
print("Left_border_Conf_Inter=",Left_border_Conf_Inter,"  Right_border_Conf_Inter=",Right_border_Conf_Inter)

#рандомизация исходных данных
A[:]=np.random.normal(mu1, SKO1, n_size_A)
B[:]=np.random.normal(mu1*0.002 + mu1, SKO1, n_size_B)

max1, min1 = max_min(A,B)


Result_All = np.concatenate([A,B])
print(len(A),"\t",len(B),"\t",len(Result_All))

#подсчет средних от данных
mean_estimate_before=np.mean(A[:]) #?
mean_estimate_after=np.mean(B[:])
mean = mean_estimate_after - mean_estimate_before
print("before",mean_estimate_before,"\n","after",mean_estimate_after)
print(mean)
#оценка стандартного отклонения (зачем нужно?)
standart_deviation_estimate_before=np.std(A[:])
standart_deviation_estimate_after=np.std(B[:])

#инициализация массивов для выборки
average_value_bootstrep_before = np.zeros([n_size_Result])
average_value_bootstrep_after = np.zeros([n_size_Result])

from sklearn.utils import resample
Delta = np.zeros([1000])

#бутстреп для 180+30

#дельта будстрепа
for i in range(1000):
    Result_All = resample(Result_All[:], replace=False )
    Result_All_Before, Result_All_After = Result_All[:n_size_A], Result_All[n_size_A:]
    Delta[i] = np.mean(Result_All_After) - np.mean(Result_All_Before)



#бутстреп
for i in range(1000):
    boot = resample(A[:], #Список c исходной выборкой
                    replace=True,  # Если ” True”, то случайная выборка с возвратом элемент 
                    n_samples=180
                    )
    average_value_bootstrep_before[i] = np.mean(boot[:])
    boot = resample(B[:], #Список c исходной выборкой
                    replace=True,  # Если ” True”, то случайная выборка с возвратом элемент 
                    n_samples=30
                    )
    average_value_bootstrep_after[i] = np.mean(boot[:])
    #Delta[i] = np.mean(average_value_bootstrep_after) - np.mean(average_value_bootstrep_before) 
    
mean_estimate_before_boot=np.mean(average_value_bootstrep_before[:]) #?
mean_estimate_after_boot=np.mean(average_value_bootstrep_after[:])
    
#************************************************************************
#%% = Начало Блока.  Если блок Выделить, то его можно выполнить Ctrl + Enter

#chr(171) - кавычки открываются 
#chr(187) - кавычки закрываются
#chr(32)  - пробел
#chr(945) - Alfa
#chr(946) - Betta
#chr(916) - Delta
#chr(956) - mu
#chr(963) - sigma


colors = ['']*15

colors[0]  ='b' #Синий
colors[1]  ='g' #Зелёный
colors[2]  ='r' #Красный
colors[3]  ='с' #Бирюзовый
colors[4]  ='b' #Фиолетовый / Пурпурный
colors[5]  ='y' #Желтый
colors[6]  ='k' #Черный
colors[7]  ='w' #Белый
colors[8]  ='goldenrod' # См. Полную Таблицу Цветов в Mathplotlib
colors[9]  ='grey' #Серый
colors[10] ='magenta' #Пурпурно-Красный
colors[11] ='floralwhite' #См. Полную Таблицу Цветов в Mathplotlib
colors[12] ='skyblue' #См. Полную Таблицу Цветов в Mathplotlib
colors[13] ='orangered'
colors[14] ='tomato'





print("\n\n\n")

#******************************************************************************
#    pass




fig, (ax3) = plt.subplots(1, 1, figsize=(12, 4))
plt.subplot(1, 1, 1)

#fig, (ax1,ax2,ax3) = plt.subplots(3, 1, figsize=(12, 18))
#plt.subplot(3, 1, 1)
#ax1.set_facecolor(colors[11])
#ax2.set_facecolor(colors[11])
ax3.set_facecolor(colors[11])

 

#prop = dict(alpha=1, lw=2, ls='-', edgecolor='black', facecolor='lightblue', zorder=0)
# "prob" - - параметры графика гистограммы - слой= 0
#          alpha - полупрозрачность
#          lw - ширирина линии
#          ls -  тип линии
#          edgecolor - цвет линии
#          facecolor - заливка гистограммы
#          zorder - это нулевой слой на графики 


#  hist - переменная, которая не используется ax1.hist  - это уже метод hist, который изменяет ax1 (то есть в ax1 добавляет
#                                                                гистограмму)
#  ax1 -  переменная, в которой находится гистограмма  
#   distr - исходная выборка
#   bins -количество карманов гистограммы
#   density=True - площадь столбцов = 1
#   prop - словаррь, где хранятся параметры гистограммы - см. выше


labels_before = ["Эксп. данные до"]
labels_after = ["Эксп. данные после"]

labels1 = ["Средние знач."]


text_before = [f'{mean_estimate_before: .2f}']  # $ - переход на нижний регистр. $ - возврат в средний регистр
      
text_after = [f'{mean_estimate_after: .2f};']  # $ - переход на нижний регистр. $ - возврат в средний регистр
   

kde_parametrs = [1] # подбирают вручную. Этот параметр убирает волнообразность
                       #Обратно к Высоте Огибающей
kde_linspace = np.zeros([1,2])   
kde_linspace[0,:]=[min1,max1] # Диапазон, в котором стороится 1-я Огибающая   

vline_before=np.zeros([1])
vline_after=np.zeros([1])
vline_before[0]=mean_estimate_before  # mu (=Сред.) для 1-вой выборки
vline_after[0]=mean_estimate_after       

from sklearn.neighbors import KernelDensity # используем класс из sklearn

   
prop_before = dict( # Параметры Отрисовки Гистограммы
                alpha=1.0, # Прозрачность
                linewidth=2,      # Толщина линии Прямоуольников
                linestyle='-',    # Стиль Линии                
                edgecolor='black', # Цвет Линии
                facecolor=colors[12], # Цвет заливки Прямогольников Гистограммы
                ) 

prop_after = dict( # Параметры Отрисовки Гистограммы
                alpha=1.0, # Прозрачность
                linewidth=2,      # Толщина линии Прямоуольников
                linestyle='-',    # Стиль Линии                
                edgecolor='black', # Цвет Линии
                facecolor="tomato", # Цвет заливки Прямогольников Гистограммы
                ) 

distr_before=A[:] # "distr" = 1D массив, в котором данные для построения Гистограммы
distr_after=B[:]

xx1 = np.linspace(*kde_linspace[0,:], 200) # См. след. строку
"""
kde = KernelDensity(bandwidth=kde_parametrs[0])  #Обратно к Высоте Огибающей !!!
kde.fit(distr_before[:,None])  # Подгонка Огибающей
logprobes = kde.score_samples(xx1[:,None])  # Огибающая стороится почему-то в логарифмах,
ax1.plot(xx1,np.exp(logprobes), lw=4, c='navy') # Рисуем Огибающую (поэтому при рисовании делаем потенциирование)

kde.fit(distr_after[:,None])
logprobes = kde.score_samples(xx1[:,None])
ax1.plot(xx1,np.exp(logprobes), lw=4, c='darkred')

ax1.hist(distr_after, 
            bins=5,
            label=labels_after[0],
            density=True,
            **prop_after)  


N = ax1.hist(  # Рассчитываем и рисуем Гистограмму
            distr_before, # 1D массив с эксперим. данными
            bins=20, # Кол-во частотных диапазонов (Карманов)
            label=labels_before[0], # Попись рядом с цветом в Легенде
            density=True,    # Гистограмма в виде Плотности Вероятности (S==1)
            **prop_before) # см. "prop" выше

#обработка переменных для их спользования в дальнейшем для диномического графика
max_g1 = N[0].max() * 1.6


ax1.vlines ( # рисуем верикаль. линии, соотвествующие Среднему (mu1)
        vline_before[0], # координата по "x"
        0, max_g1,   # Начало и Конец пр "Y"
        colors=colors[0], # Цвет Линии
        linewidth=2.5,   # Толщина линии
        linestyles='--')  # Стиль Линии 

ax1.vlines ( # рисуем верикаль. линии, соотвествующие Среднему (mu1)
        vline_after[0], # координата по "x"
        0, max_g1,   # Начало и Конец пр "Y"
        colors='maroon', # Цвет Линии
        linewidth=2.5,   # Толщина линии
        linestyles='--')  # Стиль Линии 


ax1.text ( # Подпись Вертикаль. Линий
        vline_before[0] - mu1*0.003, # "X" координата начала подписи
        y=max_g1*0.9,          # "Y" координата начала подписи
        s=text_before[0],      # Текст Подписи Вертикальной Линии
        fontsize=14)    # Размер шрифта
   
ax1.text ( # Подпись Вертикаль. Линий
        vline_after[0] + mu1*0.001, # "X" координата начала подписи
        y=max_g1*0.9,          # "Y" координата начала подписи
        s=text_after[0],      # Текст Подписи Вертикальной Линии
        fontsize=14)    # Размер шрифта

ax1.annotate( # Рисуем двойную стрелку
             text='',# Подпись у Стрелки - ОТСУТСТВУЕТ
             xy=( mean_estimate_before, max_g1*0.9), # Левые координаты (x,y) стрелки *0.9992
             xytext=(mean_estimate_after, max_g1*0.9), #  # Правые координаты (x,y) стрелки *1.0015
             arrowprops={'arrowstyle': '<->', 'lw':2}, # Тип стрелки и её толщина
            )

ax1.annotate(  # Рисуем линию для размера стрелки
            text='', # Подпись у Стрелки - ОТСУТСТВУЕТ
            xy=(mean_estimate_after*1.00, max_g1*0.8),  # Левые координаты (x,y) линии
                xytext=(mean_estimate_after*1.07, max_g1*0.8),   # Правые координаты (x,y) линии
            arrowprops={'arrowstyle': '-', 'lw':2}, # Тип линии и её толщина
            )

ax1.text ( # Подпись Вертикаль. Линий
        vline_after[0] * 1.01, # "X" координата начала подписи
        y=max_g1*0.75,          # "Y" координата начала подписи
        s='Различия между средними 2%',      # Текст Подписи Вертикальной Линии
        fontsize=14)    # Размер шрифта



ax1.set_ylim(0,max_g1) # пределы Оси "Y"
ax1.set_xlim(min1,max1) # пределы Оси "X"

ax1.set_xlabel('Измерения', fontsize=16) # Подпись под рисунком - ось "X"
ax1.set_ylabel('Плотность вероятности', fontsize=16) # Подпись осb "Y"
ax1.set_title("Распределение экспериментальных значений", fontsize=16) # # Подпись над рисунком 

ax1.legend(loc="upper right",  fontsize=12)
"""
"""
---ax1.vlines ( # рисуем верикаль. линии, соотвествующие Среднему (mu1)
        vline[0], # координата по "x"
        0, 0.06,   # Начало и Конец пр "Y"
        colors=colors[0], # Цвет Линии
        linewidth=2.5,   # Толщина линии
        linestyles='--')  # Стиль Линии 
    
---ax1.text ( # Подпись Вертикаль. Линий Mu=... Sigma=...
        x= 346, # "X" координата начала подписи #vline[0]+0.35
        y=0.05,          # "Y" координата начала подписи
        s=text[0],      # Текст Подписи
        fontsize=14)    # Размер шрифта






---ax1.vlines ( # рисуем верикаль. линии, соотвествующую 5% Пёрцентили (то есть 
                                                # 5% значений (то есть ШТУК) лежат меньше этой величины)
        np.percentile(distr, Left_border_Conf_Inter), # координата по "x"
        0, 0.05,   # Начало и Конец пр "Y"
        colors=colors[2], # Цвет Линии
        linewidth=2.5,   # Толщина линии
        linestyles='-')  # Стиль Линии 
    
--ax1.text ( # Подпись Вертикаль. Линий
        x=np.percentile(distr, Left_border_Conf_Inter)+0.009, # "X" координата начала подписи
        y=0.042,          # "Y" координата начала подписи
        s=f'{np.percentile(distr, Left_border_Conf_Inter): .2f}'+'',      # Текст Подписи Вертикальной Линии
        fontsize=14)    # Размер шрифта

#         s=chr(916)+f'={Delta_Observed: .2f}', # Текст Подписи


--ax1.vlines ( # рисуем верикаль. линии, соотвествующую 95% Пёрцентили (то есть 
                                                # 95% значений (то есть ШТУК) лежат меньше этой величины)
        np.percentile(distr, Right_border_Conf_Inter), # координата по "x"
        0, 0.05,   # Начало и Конец пр "Y"
        colors=colors[2], # Цвет Линии
        linewidth=2.5,   # Толщина линии'
        linestyles='-')  # Стиль Линии 
    
--ax1.text ( # Подпись Вертикаль. Линий
        x= np.percentile(distr, Right_border_Conf_Inter)+0.01, # "X" координата начала подписи
        y=0.042,          # "Y" координата начала подписи
        s=f'{np.percentile(distr, Right_border_Conf_Inter): .2f}'+'',      # Текст Подписи Вертикальной Линии
        fontsize=14)    # Размер шрифта



--ax1.annotate( # Рисуем двойную стрелку
             text=' ',# Подпись у Стрелки - ОТСУТСТВУЕТ
            xy=(np.percentile(distr, Left_border_Conf_Inter)*0.9992, 0.04), # Левые координаты (x,y) стрелки
                xytext=(np.percentile(distr, Right_border_Conf_Inter)*1.0015
                        , 0.04), #  # Правые координаты (x,y) стрелки
            arrowprops={'arrowstyle': '<->', 'lw':2}, # Тип стрелки и её толщина
            )

--ax1.annotate(  # Рисуем линию для размера стрелки
            text='', # Подпись у Стрелки - ОТСУТСТВУЕТ
            xy=(np.percentile(distr, Right_border_Conf_Inter)*1.00, 0.045),  # Левые координаты (x,y) линии
                xytext=(np.percentile(distr, Right_border_Conf_Inter)+22.8, 0.045),   # Правые координаты (x,y) линии
            arrowprops={'arrowstyle': '-', 'lw':2}, # Тип линии и её толщина
            )



ax1.text (   #  подписись над линией
         x=np.percentile(distr, Right_border_Conf_Inter)+0.5, y=0.046, #  координаты (x,y) подписи
         # $_ - переход на нижний регистр. $ - возврат в средний регистр
         s=f'{Confidence_Interval}' + "% Довер. Интервал", # Текст Подписи
         fontsize=16, # Размер Шрифта
          color='black') # Цвет Подписи




Left_border_Conf_Inter=Confidence_Interval_New

ax1.vlines ( # рисуем верикаль. линии, соотвествующую 5% Пёрцентили (то есть 
                                                # 5% значений (то есть ШТУК) лежат меньше этой величины)
        np.percentile(distr, Left_border_Conf_Inter), # координата по "x"
        0, 0.056,   # Начало и Конец пр "Y"
        colors=colors[2], # Цвет Линии
        linewidth=2.5,   # Толщина линии
        linestyles='-')  # Стиль Линии 







ax1.set_xlabel('Измерения', fontsize=16) # Подпись под рисунком - ось "X"
ax1.set_ylabel('Плотность вероятности', fontsize=16) # Подпись осb "Y"
ax1.set_title("Распределение экспериментальных значений", fontsize=16) # # Подпись над рисунком 


#ax1.legend(loc="lower right")
#ax1.legend(loc="upper left")
ax1.legend(loc="upper right",  fontsize=12)
#ax1.legend(loc="lower left")


ax1.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
"""
#******************************************************************************
"""
kde_parametrs1 = [0.15]
distr1_before=average_value_bootstrep_before[:] # "distr" = 1D массив, в котором данные для построения Гистограммы
distr1_after=average_value_bootstrep_after[:]

max1, min1 = max_min(average_value_bootstrep_before,average_value_bootstrep_after)

kde_linspace1 = np.zeros([1,2])
kde_linspace1[0,:]=[min1,max1] # Диапазон, в котором стороится 1-я Огибающая

xx2 = np.linspace(*kde_linspace1[0,:], 200) # См. след. строку
kde1 = KernelDensity(bandwidth=kde_parametrs1[0])  #Обратно к Высоте Огибающей !!!

kde1.fit(distr1_before[:,None])  # Подгонка Огибающей

logprobes = kde1.score_samples(xx2[:,None])  # Огибающая стороится почему-то в логарифмах,
ax2.plot(xx2,np.exp(logprobes), lw=4, c='navy') # Рисуем Огибающую (поэтому при рисовании делаем потенциирование)


kde1.fit(distr1_after[:,None])

logprobes = kde1.score_samples(xx2[:,None])  # Огибающая стороится почему-то в логарифмах,
ax2.plot(xx2,np.exp(logprobes), lw=4, c='darkred') # Рисуем Огибающую (поэтому при рисовании делаем потенциирование)


N = ax2.hist(  # Рассчитываем и рисуем Гистограмму
            distr1_before, # 1D массив с эксперим. данными
            bins=20, # Кол-во частотных диапазонов (Карманов)
            label=labels_before[0], # Попись рядом с цветом в Легенде
            density=True,    # Гистограмма в виде Плотности Вероятности (S==1)
            **prop_before) # см. "prop" выше

#обработка переменных для их спользования в дальнейшем для диномического графика
max_g1 = N[0].max() * 1.6

ax2.hist(  # Рассчитываем и рисуем Гистограмму
            distr1_after, # 1D массив с эксперим. данными
            bins=10, # Кол-во частотных диапазонов (Карманов)
            label=labels_after[0], # Попись рядом с цветом в Легенде
            density=True,    # Гистограмма в виде Плотности Вероятности (S==1)
            **prop_after) # см. "prop" выше


   # ax1.vlines (vline[j], 0, 6, colors='black', lw=2.5, linestyles='dashed', zorder=3)

ax2.vlines ( # рисуем верикаль. линии, соотвествующие Среднему (mu1)
        mean_estimate_before_boot, # координата по "x"
        0, max_g1,   # Начало и Конец пр "Y"
        colors=colors[0], # Цвет Линии
        linewidth=2.5,   # Толщина линии
        linestyles='--')  # Стиль Линии 

ax2.vlines ( # рисуем верикаль. линии, соотвествующие Среднему (mu1)
        mean_estimate_after_boot, # координата по "x"
        0, max_g1,   # Начало и Конец пр "Y"
        colors='maroon', # Цвет Линии
        linewidth=2.5,   # Толщина линии
        linestyles='--')  # Стиль Линии 

Left_border_Conf_Inter=Confidence_Interval_New


ax2.set_ylim(0,max_g1)#(0,1.4) # пределы Оси "Y"
ax2.set_xlim(min1,max1)#(345,425)####(381,384) # пределы Оси "X"

ax2.set_xlabel('Измерения', fontsize=16) # Подпись под рисунком - ось "X"
ax2.set_ylabel('Плотность вероятности', fontsize=16) # Подпись осb "Y"
ax2.set_title("Распределение средних значений", fontsize=16) # # Подпись над рисунком 


#ax1.legend(loc="lower right")
#ax1.legend(loc="upper left")
ax2.legend(loc="upper right",  fontsize=12)
#ax1.legend(loc="lower left")


ax2.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
"""

labels_all = ["Разность средних"]
kde_parametrs1 = [0.1]
distr_delta=Delta[:] # "distr" = 1D массив, в котором данные для построения Гистограммы

kde_linspace1 = np.zeros([1,2])
kde_linspace1[0,:]=[min(Delta)*1.3,max(Delta)*1.3]
kde_linspace2 = np.zeros([1,2])
kde_linspace2[0,:]=[mean,max(Delta)*1.3]

xx3_ = np.linspace(*kde_linspace2[0,:], 1000) # См. след. строку
xx3 = np.linspace(*kde_linspace1[0,:], 1000) # См. след. строку


kde3 = KernelDensity(bandwidth=kde_parametrs1[0])  #Обратно к Высоте Огибающей !!!
kde3.fit(distr_delta[:,None])  # Подгонка Огибающей

logprobes = kde3.score_samples(xx3[:,None])  # Огибающая стороится почему-то в логарифмах,
logprobes_ = kde3.score_samples(xx3_[:,None])
ax3.plot(xx3,np.exp(logprobes), lw=4, c='navy') # Рисуем Огибающую (поэтому при рисовании делаем потенциирование)
ax3.plot(xx3_,np.exp(logprobes_), lw=4, c="darkred")


        
l = len(np.exp(logprobes_))
#for i in range(l):
#    print("%0.4f"%np.exp(logprobes_)[i],"\n")
    
N = ax3.hist(  # Рассчитываем и рисуем Гистограмму
            distr_delta, # 1D массив с эксперим. данными
            bins=20, # Кол-во частотных диапазонов (Карманов)
            label=labels_all[0], # Попись рядом с цветом в Легенде
            density=True,    # Гистограмма в виде Плотности Вероятности (S==1)
            **prop_before) # см. "prop" выше

#обработка переменных для их спользования в дальнейшем для диномического графика
max_g1 = N[0].max() * 1.6


#Другйо способ нахождения площади
p_level=(100-st.percentileofscore(distr_delta,mean)) / 100




ax3.vlines ( # рисуем верикаль. линии, соотвествующую 5% Пёрцентили (то есть 
                                                # 5% значений (то есть ШТУК) лежат меньше этой величины)
        mean, # координата по "x"
        0, max_g1,   # Начало и Конец пр "Y"
        colors="darkred", # Цвет Линии
        linewidth=2.5,   # Толщина линии
        linestyles='--')  # Стиль Линии 

ax3.vlines ( # рисуем верикаль. линии, соотвествующую 5% Пёрцентили (то есть 
                                                # 5% значений (то есть ШТУК) лежат меньше этой величины)
        0, # координата по "x"
        0, max_g1,   # Начало и Конец пр "Y"
        colors=colors[6], # Цвет Линии
        linewidth=2,   # Толщина линии
        linestyles='-')  # Стиль Линии

ax3.fill_between(xx3_, np.exp(logprobes_),color='red', alpha  = 0.3)


#
n0 = 0
nn = 0
bo = True
#print("Полезные y:")
for i in range(len(np.exp(logprobes))):
    if round(np.exp(logprobes)[i], 4) != 0.:
        nn += 1
        bo = False
    elif bo:
        n0 += 1

        
mat = np.zeros(nn) 

for i in range(n0 + nn):#nn):#
    if i > n0:
        mat[i - n0] = round(np.exp(logprobes)[i],4)
        #print(mat[i - n0],end = " ")


n = max(Delta) - min(Delta)
print("Всего полезных элементов:",nn,"\nДлина полезная:", n)

area = np.trapz(mat, dx = n / nn)
print("Вся площадь:",area)

"""
norm_rv = st.norm(loc=distr_delta.mean(), scale=distr_delta.std())
p = 1 - norm_rv.cdf(mean)
print("Ещё некая площадь:",p)
"""

nn = 0
for i in range(len(np.exp(logprobes_))):
    if round(np.exp(logprobes_)[i], 4) != 0.:
        nn += 1
        
mat = np.zeros(nn) 

for i in range(nn):
    mat[i] = round(np.exp(logprobes_)[i],4)

#print("Полезные y:")
l = len(mat)
#for i in range(l):
#    print("%0.4f"%mat[i],end = " ")

print("\nДлина mat: ",len(mat) )

n = max(Delta) - mean
print("Всего полезных элементов:",nn,"\nДлина полезная:", n)

area = np.trapz(mat, dx = n / nn)


ax3.text ( # Подпись Вертикаль. Линий
        max(Delta)*0.7, # "X" координата начала подписи
        y=max_g1*0.5,          # "Y" координата начала подписи
        s='Площадь под\nграфиком: %.3f'%area,      # Текст Подписи Вертикальной Линии
        fontsize=14) 

ax3.set_ylim(0,max_g1)
ax3.set_xlim(min(Delta)*1.3,max(Delta)*1.3)

ax3.set_xlabel('Разность средних', fontsize=16) # Подпись под рисунком - ось "X"
ax3.set_ylabel('Плотность вероятности', fontsize=16) # Подпись осb "Y"
ax3.set_title("Распределение разность средних", fontsize=16) # # Подпись над рисунком 

ax3.legend(loc="upper right",  fontsize=12)

ax3.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )



print("Средние:\n",np.mean(A),"\n",np.mean(average_value_bootstrep_before),"\n",
      np.mean(B),"\n",np.mean(average_value_bootstrep_after))
##%% == Конец Блока
print("Площадь: ",area)
norm_rv = st.norm(loc=distr_delta.mean(), scale=distr_delta.std())
p = 1 - norm_rv.cdf(mean)

print("\n\nНахождение площади через scipy.stats:",p_level)
print("Нахождение площади дубовым методом", area)
print("Ещё некая площадь:",p)


#******************************************************************************

n_size_Effect=1000 # Размер массива Effect
Effect = np.zeros([n_size_Effect]) # Объявляем массив

A_i = np.zeros([n_size_A]) # Объявляем массив
B_i = np.zeros([n_size_B]) # Объявляем массив

for i in range(n_size_Effect): # цикл
    A_i = resample(A, replace=True)              # делаем бутстреп "повтор" массива А
    B_i = resample(B, replace=True)              # делаем бутстреп "повтор" массива B
    Effect[i] = 100* (np.mean(B_i) - np.mean(A_i[:])) / np.mean(A_i[:])     # получаем массив

#******************************************************************************
Alfa=0.1
Delta_Critich=np.percentile(Delta,100-Alfa*100)

n_size_Metrics_in_effect=1000 # Размер массива Effect
Metrics_in_effect = np.zeros([n_size_Metrics_in_effect]) # Объявляем массив

A_i = np.zeros([n_size_A]) # Объявляем массив
B_i = np.zeros([n_size_B]) # Объявляем массив


for i in range(n_size_Metrics_in_effect): # цикл

    A_i = resample(A, replace=True) # делаем бутстреп "повтор" массива А
    B_i = resample(B, replace=True) # делаем бутстреп "повтор" массива B
    
    Metrics_in_effect[i]=np.mean(B_i) - np.mean(A_i[:])# получаем массив эффектов


Betta =  (Metrics_in_effect < Delta_Critich).sum() / n_size_Effect


#******************************************************************************
class Ploter():
    def __init__(self, name):
        self.name = name
        self.fig, self.ax = plt.subplots(figsize=(12, 4))
        #self.ax.set_facecolor()
        print("Hello World, " + self.name)      
        self.prop = dict( # Параметры Отрисовки Гистограммы
                        alpha=1.0, # Прозрачность
                        linewidth=2,      # Толщина линии Прямоуольников
                        linestyle='-',    # Стиль Линии                
                        edgecolor='black', # Цвет Линии
                        facecolor="tomato")
        
        
    def plot_hist(self, distr,bins):
        self.distr = distr
        Set = self.ax.hist(self.distr, 
                    bins,
                    label=self.name,
                    density=True,
                    **self.prop) 
        self.max_y = Set[0].max() * 1.5
    

    def plot_kde(self,kde_parametrs, steps = 1000, left = None, right = None  ):
        kde_linspace = np.zeros([1,2])
        if left is None:
            left = min(self.distr)*1.3
            
        if right is None:
            right = max(self.distr)*1.3
        kde_linspace[0,:]=[left, right]
        x = np.linspace(*kde_linspace1[0,:], steps)
        kde = KernelDensity(bandwidth=kde_parametrs)
        kde.fit(self.distr[:,None]) 
        logprobes = kde.score_samples(x[:,None])
        self.ax.plot(x,np.exp(logprobes), lw=4, c='navy')
    
    def plot_mean(self):
        self.plot_line(np.mean(self.distr[:]))
       
        
    def plot_line(self, x):
        self.ax.vlines (x, # координата по "x"
                0, self.max_y,   # Начало и Конец пр "Y"
                colors=colors[6], # Цвет Линии
                linewidth=2.5,   # Толщина линии
                linestyles='--')  # Стиль Линии 
    def plot_p_level(self, Critich,delta):
        
        self.ax.vlines (delta, # координата по "x"
                0, max_g1,   # Начало и Конец пр "Y"
                colors=colors[2], # Цвет Линии
                linewidth=4.5,   # Толщина линии
                linestyles='-')  # Стиль Линии 
        
        
        
        
a1 = Ploter("a1")

a1.plot_hist(distr_delta, 20)
a1.plot_kde(0.08)
a1.plot_mean()



print("\n\n\n")
stop


fig, (ax4) = plt.subplots(1, 1, figsize=(12, 5))
plt.subplot(1, 1, 1)
#ax1.set_facecolor(colors[11])

text = [chr(956)+'$_'+chr(916)+'$'+'$_{при}$'+ chr(32)+'$_{ОТКЛОНЕНИИ}$'+ chr(32)+'$_{ Н0}$ =', # $ - переход на нижний регистр. $ - возврат в средний регистр
        'Граница ошибки 1-го рода']

kde_parametrs1 = [0.1]
distr_effect=Metrics_in_effect[:] # "distr" = 1D массив, в котором данные для построения Гистограммы

kde_linspace1 = np.zeros([1,2])
kde_linspace1[0,:]=[min(distr_effect)*1.3,max(distr_effect)*1.3]
kde_linspace2 = np.zeros([1,2])
kde_linspace2[0,:]=[min(distr_effect)*1.3,Delta_Critich]

xx4_ = np.linspace(*kde_linspace2[0,:], 1000) # См. след. строку
xx4 = np.linspace(*kde_linspace1[0,:], 1000) # См. след. строку


kde4 = KernelDensity(bandwidth=kde_parametrs1[0])  #Обратно к Высоте Огибающей !!!
kde4.fit(distr_effect[:,None])  # Подгонка Огибающей

logprobes = kde4.score_samples(xx4[:,None])  # Огибающая стороится почему-то в логарифмах,
logprobes_ = kde4.score_samples(xx4_[:,None])
ax4.plot(xx4,np.exp(logprobes), lw=4, c='navy') # Рисуем Огибающую (поэтому при рисовании делаем потенциирование)
ax4.plot(xx4_,np.exp(logprobes_), lw=4, c="darkred")


N = ax4.hist(  # Рассчитываем и рисуем Гистограмму
            distr_effect, # 1D массив с эксперим. данными
            bins=20, # Кол-во частотных диапазонов (Карманов)
            label=labels_all[0], # Попись рядом с цветом в Легенде
            density=True,    # Гистограмма в виде Плотности Вероятности (S==1)
            **prop_before) # см. "prop" выше

max_g1 = N[0].max() * 1.6


ax4.vlines ( # рисуем верикаль. линии, соотвествующую Среднему (mu2)
        # линия=СРЕДНЕМУ
        np.mean(Metrics_in_effect[:]), # координата по "x"
        0, max_g1,   # Начало и Конец пр "Y"
        colors=colors[14], # Цвет Линии
        linewidth=2.5,   # Толщина линии
        linestyles='--')  # Стиль Линии 

    
ax4.vlines ( # рисуем верикаль. линии, соотвествующую  Значение Эффекта в  Пилот. Проекта
        # линия = ГРАНИЦЕ Alfa   
        Delta_Critich, # координата по "x"
        0, max_g1,   # Начало и Конец пр "Y"
        colors=colors[2], # Цвет Линии
        linewidth=4.5,   # Толщина линии
        linestyles='-')  # Стиль Линии 

ax4.annotate("  =" +f'{Betta: .2f}', fontsize=18, xytext=(-0.09,max_g1*0.9),# координаты надписи и Начала Стрелки 
                                          xy = (Delta_Critich-0.04, max_g1*0.4), # координаты окончания стрелки
                color=colors[2],
                arrowprops=dict(color=colors[6], # рисуем кривую стрелку
                                linewidth=2,
                                arrowstyle='->',
                                connectionstyle='angle3,'+ # управляющий параметр(могут быть разные стрелки - см. Примеры в InterNet
                                'angleA=195,'+ # Угол выхода из Началь. точки - А
                                'angleB=333'))# Угол входа в конечную точку - В

ax4.text ( # Подпись Вертикаль. Линий
        x=Delta_Critich*1.8, # "X" координата начала подписи
        y=max_g1*0.65,          # "Y" координата начала подписи
        s="Граница ошибки 1-го рода",
         c=colors[2],
        fontsize=16)    # Размер шрифта

ax4.text ( # Подпись Вертикаль. Линий
        x=Delta_Critich*1.1, # "X" координата начала подписи
        y=max_g1*0.85,          # "Y" координата начала подписи
        #s=chr(956)+'$_{}$'+f'={mean_estimate_B: .2f}', # $_ - переход на нижний регистр. $ - возврат в средний регистр
        s=text[0],
        c=colors[14],
        fontsize=20)    # Размер шрифта

ax4.annotate("", fontsize=18, xytext=(Delta_Critich*1.8,max_g1*0.65),# координаты надписи и Начала Стрелки 
                                          xy = (Delta_Critich, max_g1*0.4), # координаты окончания стрелки
                color=colors[2],
                arrowprops=dict(color=colors[2], # рисуем кривую стрелку
                                linewidth=2,
                                arrowstyle='->',
                                connectionstyle="angle3,"+ # управляющий параметр(могут быть разные стрелки - см. Примеры в InterNet
                                "angleA=250,"+ # Угол выхода из Началь. точки - А
                                "angleB=20"))# Угол входа в конечную точку - В

ax4.text ( # Подпись Вертикаль. Линий
        x=Delta_Critich*1.1, # "X" координата начала подписи
        y=max_g1*0.75,          # "Y" координата начала подписи
        #s=chr(956)+'$_{}$'+f'={mean_estimate_B: .2f}', # $_ - переход на нижний регистр. $ - возврат в средний регистр
        s='='+f'{np.mean(Metrics_in_effect[:]): .3f}' ,
        c=colors[14],
        fontsize=20)    # Размер шрифта

ax4.fill_between(xx4_, np.exp(logprobes_),color='red', alpha  = 0.5)
ax4.set_title("Распределение разность средних", fontsize=16) # # Подпись над рисунком 

ax4.legend(loc="upper right",  fontsize=12)

ax4.set_ylim(0,max_g1)
ax4.set_xlim(min(distr_effect)*1.3,max(distr_effect)*1.1)



























plt.show()

#print("56  kde_parametrs=",kde_parametrs)

#******************************************************************************
