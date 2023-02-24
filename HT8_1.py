# 1)Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

salary = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
credit_scoring = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.

# 1) Находим ковариацию по формуле:
cov = np.mean(salary*credit_scoring) - np.mean(salary) * np.mean(credit_scoring)    # 9157.839999999997
print(f'Ковариация по формуле: {cov}')

# 2) С помощью функции numpy:
cov_np = np.cov(salary, credit_scoring, ddof=0) # 9157.84
print('Корреляция по функции:', cov_np)

# 3) Находим коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений:
coef_Pearsons = cov_np/(np.std(salary, ddof=0) * np.std(credit_scoring, ddof=0)) # 0.88749009
print(f'Коэффициент Пирсона по формуле: {coef_Pearsons}')

# 4) C использованием функций из библиотек numpy и pandas:
coef_stats = stats.pearsonr(salary, credit_scoring)
print('Коэффициент Пирсона по функции:', coef_stats)    # 0.8874900920739162
plt.scatter(salary, credit_scoring)
plt.title( 'coef_Pearson = 0.88749009')
plt.xlabel('salary')
plt.ylabel('credit_scoring')
plt.show()
