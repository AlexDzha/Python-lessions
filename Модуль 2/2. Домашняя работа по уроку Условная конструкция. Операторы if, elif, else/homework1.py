first = int(input('Введите число:  '))
second = int(input('Введите число:  '))
third = int(input('Введите число:  '))
if first == second and second == third:
    print('Количество одинаковых чисел: 3')
elif first == second or second == third or first == third:
    print('Количество одинаковых чисел: 2')
else:
    print('Количество одинаковых чисел: 0')