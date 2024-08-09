# Создаем функуцию divide, которая принимает два параметра (first и second).
def divide(first, second):
    # Деление на 0 возращает ошибку
    if second == 0:
        return 'Ошибка'
    # Hезультат деления first на second
    else:
        return first / second

