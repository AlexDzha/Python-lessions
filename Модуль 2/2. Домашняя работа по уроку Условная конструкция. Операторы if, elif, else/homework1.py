first = int(input('Введите число:  '))
second = int(input('Введите число:  '))
third = int(input('Введите число:  '))
if first == second == third:
    print('Кол-во одинаковых чисел: 3')
elif first == second or second == third or first == third:
    print('Кол-во одинаковых чисел: 2')
else:
    print('Кол-во одинаковых чисел: 0')