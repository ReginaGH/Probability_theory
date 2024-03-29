# ДЗ №6, задача 1. Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением, 
# равным 16. # Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95,
# если выборочная средняя M = 80, а объем выборки n = 256.

# Вводные данные:
sigma = 16
alpha = 0.05
x = 80
n = 256

import numpy as np
import scipy.stats as stats

# 1) Найдём Z-критерий для alpha = 0.05/2
z = stats.norm.ppf(1-alpha/2)   # 1.959963984540054
print(f'Табличный Z-критерий для alpha/2: {z}')

# 2) Находим границы интервала:
low = x - z * sigma/np.sqrt(n)  # 78.04003601545995
up = x + z * sigma/np.sqrt(n)   # 81.95996398454005
print(f'Доверительный интервал [{low} ; {up}]')