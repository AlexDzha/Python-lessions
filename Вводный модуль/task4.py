# "4th program"
print('"4th program"')
string_number = '123.456'
float_number = float(string_number)  # Преобразуем строку в дробное число
shifted_number = float_number * 10   # Умножаем на 10, чтобы сместить 4 в целую часть
first_digit_after_dot = int(shifted_number) % 10  # Берем остаток от деления на 10

print(first_digit_after_dot)  # Ожидаемый результат: 4
