# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 09:51:40 2021

@author: Mavrin S.V.

Для домашнего выполнения лаб. работ необходимо:
    1. Установить пакет Anaconda: https://repo.anaconda.com/archive/Anaconda3-2022.05-Windows-x86_64.exe
    2. После установки запустить Spyder
    3. Открыть этот файл и выполнить программу.


"""


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
#import Bootstrep as bs

Start_random_seed=85
np.random.seed(Start_random_seed)


n_size_Result=1000

Result = np.zeros([n_size_Result])

kk = 8


mu1=382                                                                        #mu1=50
SKO1=0.03*mu1
print("mu1=",mu1,"  SKO1=",SKO1)

Confidence_Interval=np.random.randint(85, 95)
Confidence_Interval=85  
Confidence_Interval_New=30


print("Confidence_Interval=",Confidence_Interval)

Left_border_Conf_Inter=(100-Confidence_Interval)/2
Right_border_Conf_Inter=Confidence_Interval + Left_border_Conf_Inter
print("Left_border_Conf_Inter=",Left_border_Conf_Inter,"  Right_border_Conf_Inter=",Right_border_Conf_Inter)
#stop



Result[:]=np.random.normal(mu1, SKO1, n_size_Result)
mean_estimate=np.mean(Result[:])
standart_deviation_estimate=np.std(Result[:])
print("mean_estimate=%.2f" %mean_estimate)
print("standart_deviation_estimate=%.3f" %standart_deviation_estimate)




mean_estimate=np.mean(Result[:])
standart_deviation_estimate=np.std(Result[:])



print("mean_estimate=%.2f" %mean_estimate)
print("standart_deviation_estimate=%.3f" %standart_deviation_estimate)


average_value_bootstrep = np.zeros([n_size_Result])
#stop

#бутстреп
from sklearn.utils import resample 
for i in range(1000):
    boot = resample(Result[:], #Список c исходной выборкой
                    replace=True,  # Если ” True”, то случайная выборка с возвратом элемент 
                    n_samples=1000
                    )
    average_value_bootstrep[i] = np.mean(boot[:])

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

fig, (ax1,ax2) = plt.subplots(2, 1, figsize=(12, 12))
plt.subplot(2, 1, 1)
ax1.set_facecolor(colors[11])
ax2.set_facecolor(colors[11])

 

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



labels = ["Эксп. Данные"]
labels1 = ["Средние знач. "]
 

text = [chr(956)+'$_{1}$'+f'={mean_estimate: .2f};' +  # $ - переход на нижний регистр. $ - возврат в средний регистр
        chr(32)*1+chr(963)+'$_{1}$'+f'={standart_deviation_estimate: .2f}' ]  # $ - переход на нижний регистр. $ - возврат в средний регистр
      



kde_parametrs = [3] # подбирают вручную. Этот параметр убирает волнообразность
                       #Обратно к Высоте Огибающей 
                 
kde_linspace = np.zeros([1,2])
kde_linspace[0,:]=[340,430] # Диапазон, в котором стороится 1-я Огибающая


vline=np.zeros([1])
vline[0]=mean_estimate  # mu (=Сред.) для 1-вой выборки


from sklearn.neighbors import KernelDensity # используем класс из sklearn

prop = dict( # Параметры Отрисовки Гистограммы
                alpha=1.0, # Прозрачность
                linewidth=2,      # Толщина линии Прямоуольников
                linestyle='-',    # Стиль Линии                
                edgecolor='black', # Цвет Линии
                facecolor=colors[12], # Цвет заливки Прямогольников Гистограммы
                ) 
    
distr=Result[:] # "distr" = 1D массив, в котором данные для построения Гистограммы

xx1 = np.linspace(*kde_linspace[0,:], 200) # См. след. строку
#xx1 = np.linspace(0.3, 1.1, 200) # Огибающая строутся от "0.3" до "1.1"  и разбивается на "200" литейных участков

kde = KernelDensity(bandwidth=kde_parametrs[0])  #Обратно к Высоте Огибающей !!!
kde.fit(distr[:,None])  # Подгонка Огибающей

logprobes = kde.score_samples(xx1[:,None])  # Огибающая стороится почему-то в логарифмах,
ax1.plot(xx1,np.exp(logprobes), lw=4, c=colors[6]) # Рисуем Огибающую (поэтому при рисовании делаем потенциирование)


print("type(distr)=",type(distr))
print("np.shape(distr)=",np.shape(distr))
print("np.size(distr)=",np.size(distr)) 
    
ax1.hist(  # Рассчитываем и рисуем Гистограмму
            distr, # 1D массив с эксперим. данными
            bins=20, # Кол-во частотных диапазонов (Карманов)
            label=labels[0], # Попись рядом с цветом в Легенде
            density=True,    # Гистограмма в виде Плотности Вероятности (S==1)
            **prop) # см. "prop" выше


   # ax1.vlines (vline[j], 0, 6, colors='black', lw=2.5, linestyles='dashed', zorder=3)
ax1.vlines ( # рисуем верикаль. линии, соотвествующие Среднему (mu1)
        vline[0], # координата по "x"
        0, 0.06,   # Начало и Конец пр "Y"
        colors=colors[0], # Цвет Линии
        linewidth=2.5,   # Толщина линии
        linestyles='--')  # Стиль Линии 
    
ax1.text ( # Подпись Вертикаль. Линий Mu=... Sigma=...
        x= 346, # "X" координата начала подписи #vline[0]+0.35
        y=0.05,          # "Y" координата начала подписи
        s=text[0],      # Текст Подписи
        fontsize=14)    # Размер шрифта





#"""
ax1.vlines ( # рисуем верикаль. линии, соотвествующую 5% Пёрцентили (то есть 
                                                # 5% значений (то есть ШТУК) лежат меньше этой величины)
        np.percentile(distr, Left_border_Conf_Inter), # координата по "x"
        0, 0.05,   # Начало и Конец пр "Y"
        colors=colors[2], # Цвет Линии
        linewidth=2.5,   # Толщина линии
        linestyles='-')  # Стиль Линии 
    
ax1.text ( # Подпись Вертикаль. Линий
        x=np.percentile(distr, Left_border_Conf_Inter)+0.009, # "X" координата начала подписи
        y=0.042,          # "Y" координата начала подписи
        s=f'{np.percentile(distr, Left_border_Conf_Inter): .2f}'+'',      # Текст Подписи Вертикальной Линии
        fontsize=14)    # Размер шрифта

#         s=chr(916)+f'={Delta_Observed: .2f}', # Текст Подписи

#"""
ax1.vlines ( # рисуем верикаль. линии, соотвествующую 95% Пёрцентили (то есть 
                                                # 95% значений (то есть ШТУК) лежат меньше этой величины)
        np.percentile(distr, Right_border_Conf_Inter), # координата по "x"
        0, 0.05,   # Начало и Конец пр "Y"
        colors=colors[2], # Цвет Линии
        linewidth=2.5,   # Толщина линии'
        linestyles='-')  # Стиль Линии 
    
ax1.text ( # Подпись Вертикаль. Линий
        x= np.percentile(distr, Right_border_Conf_Inter)+0.01, # "X" координата начала подписи
        y=0.042,          # "Y" координата начала подписи
        s=f'{np.percentile(distr, Right_border_Conf_Inter): .2f}'+'',      # Текст Подписи Вертикальной Линии
        fontsize=14)    # Размер шрифта

#"""

ax1.annotate( # Рисуем двойную стрелку
             text=' ',# Подпись у Стрелки - ОТСУТСТВУЕТ
            xy=(np.percentile(distr, Left_border_Conf_Inter)*0.9992, 0.04), # Левые координаты (x,y) стрелки
                xytext=(np.percentile(distr, Right_border_Conf_Inter)*1.0015
                        , 0.04), #  # Правые координаты (x,y) стрелки
            arrowprops={'arrowstyle': '<->', 'lw':2}, # Тип стрелки и её толщина
            )
#"""
ax1.annotate(  # Рисуем линию для размера стрелки
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






ax1.set_ylim(0,0.06) # пределы Оси "Y"
ax1.set_xlim(345,425) # пределы Оси "X"

ax1.set_xlabel('Измерения', fontsize=16) # Подпись под рисунком - ось "X"
ax1.set_ylabel('Плотность вероятности', fontsize=16) # Подпись осb "Y"
ax1.set_title("Распределение экспериментальных значений", fontsize=16) # # Подпись над рисунком 


#ax1.legend(loc="lower right")
#ax1.legend(loc="upper left")
ax1.legend(loc="upper right",  fontsize=12)
#ax1.legend(loc="lower left")


ax1.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )

#******************************************************************************
kde_parametrs1 = [0.11]
distr1=average_value_bootstrep[:] # "distr" = 1D массив, в котором данные для построения Гистограммы
kde_linspace1 = np.zeros([1,2])
kde_linspace1[0,:]=[370,390] # Диапазон, в котором стороится 1-я Огибающая
xx2 = np.linspace(*kde_linspace1[0,:], 200) # См. след. строку
kde1 = KernelDensity(bandwidth=kde_parametrs1[0])  #Обратно к Высоте Огибающей !!!

kde1.fit(distr1[:,None])  # Подгонка Огибающей

logprobes = kde1.score_samples(xx2[:,None])  # Огибающая стороится почему-то в логарифмах,
ax2.plot(xx2,np.exp(logprobes), lw=4, c=colors[6]) # Рисуем Огибающую (поэтому при рисовании делаем потенциирование)



ax2.hist(  # Рассчитываем и рисуем Гистограмму
            distr1, # 1D массив с эксперим. данными
            bins=20, # Кол-во частотных диапазонов (Карманов)
            label=labels1[0], # Попись рядом с цветом в Легенде
            density=True,    # Гистограмма в виде Плотности Вероятности (S==1)
            **prop) # см. "prop" выше


   # ax1.vlines (vline[j], 0, 6, colors='black', lw=2.5, linestyles='dashed', zorder=3)



Left_border_Conf_Inter=Confidence_Interval_New


ax2.set_ylim(0,0.06)#(0,1.4) # пределы Оси "Y"
ax2.set_xlim(345,425)#(381,384) # пределы Оси "X"

ax2.set_xlabel('Измерения', fontsize=16) # Подпись под рисунком - ось "X"
ax2.set_ylabel('Плотность вероятности', fontsize=16) # Подпись осb "Y"
ax2.set_title("Распределение средних значений", fontsize=16) # # Подпись над рисунком 


#ax1.legend(loc="lower right")
#ax1.legend(loc="upper left")
ax2.legend(loc="upper right",  fontsize=12)
#ax1.legend(loc="lower left")


ax2.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )


#******************************************************************************





plt.show()

print("99999 -", end="")
print("56  kde_parametrs=",kde_parametrs)


##%% == Конец Блока
#******************************************************************************
