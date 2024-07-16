import random

first_number = random.randint(3, 20)
result = []
print(f'Число в первой вставке: {first_number}')
for i in range(1, 20):
    for j in range(1, 20):
        if first_number % (i + j) == 0 and j > i:
            result.append(i)
            result.append(j)
result1 = ''
for n in result:
    result1 += str(n)
print('Решение:', result1)