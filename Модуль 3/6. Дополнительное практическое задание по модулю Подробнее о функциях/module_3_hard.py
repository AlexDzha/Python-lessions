# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности


#объявим функцию calculate_structure_sum с неизвестным ко-вом аргументов
def calculate_structure_sum(*data_structure):
    sum = 0
    for n in data_structure: #цикл для каждого аргумента функции
        if isinstance(n, (int, float)): #проверка на числовой тип данных (целое/с плавующей запятой)
            return n
        elif isinstance(n, str): # проверка на строковый тип данных
            return len(n)
        elif isinstance(n, (list, tuple, set)): #проверка на список, кортеж или множество
            for item in n:
                sum += calculate_structure_sum(item)
        elif isinstance(n, dict): #проверка на словарь
            for key, value in n.items():
                sum += calculate_structure_sum(key) #сумма ключей
                sum += calculate_structure_sum(value) #сумма значений
    return sum
# Входные данные:
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print("Сумма всех чисел и длин всех строк: ",result)