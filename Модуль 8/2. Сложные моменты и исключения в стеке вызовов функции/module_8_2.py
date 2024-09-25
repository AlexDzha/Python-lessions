def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        elif isinstance(a, (list, tuple, set)) and isinstance(b, (list, tuple, set)):
            return a + b
        elif isinstance(a, dict) and isinstance(b, dict):
            result = a.copy()
            result.update(b)
            return result
        else:
            return str(a) + str(b)
    except TypeError:
        return "Невозможно сложить данные типы"

# Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up([1, 2, 3], [4, 5, 6]))
print(add_everything_up({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))
print(add_everything_up(123, [1, 2, 3]))
