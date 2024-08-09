# Цель: закрепить навык создания и импортирования модулей,
# а так же функций и переменных находящихся в них.

# Из модуля fake_math импортируем функцию divide назвав ее d_t
from fake_math import divide as d_f
# Из модуля true_math импортируем функцию divide назвав ее d_f
from true_math import divide as d_t
# Исходный код
result1 = d_f(69, 3)
result2 = d_f(3, 0)
result3 = d_t(49, 7)
result4 = d_t(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)