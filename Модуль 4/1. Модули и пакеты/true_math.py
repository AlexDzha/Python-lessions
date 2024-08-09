# Импортируем бесконечность из встроенной библиотеки
from math import inf
#Создаем функуцию divide, которая принимает два параметра (first и second).
def divide(first, second):
    # Деление на 0 возращает бесконечность
    if second == 0:
        return inf
    # Hезультат деления first на second
    else:
        return first / second