# Импорты необходимых модулей
from time import sleep
from datetime import datetime
from threading import Thread

# Объявление функции write_words
def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        file.write( f'Шиншила №  {i+1}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

# Взятие текущего времени
time_start = datetime.now()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
time_stop = datetime.now()
time_res = time_stop - time_start

# Вывод разницы начала и конца работы функций
print(f'Работа функций заняла: {time_res} сек.')

# Взятие текущего времени
time2_start = datetime.now()

# Создание и запуск потоков с аргументами из задачи
Thread_first = Thread(target=write_words, args= (10, 'example5.txt'))
Thread_second = Thread(target=write_words, args= (30, 'example6.txt'))
Thread_third = Thread(target=write_words, args= (200, 'example7.txt'))
Thread_fourh = Thread(target=write_words, args= (100, 'example8.txt'))

Thread_first.start()
Thread_second.start()
Thread_third.start()
Thread_fourh.start()

Thread_first.join()
Thread_second.join()
Thread_third.join()
Thread_fourh.join()

# Взятие текущего времени

time2_stop = datetime.now()
time2_res = time2_stop - time2_start
# Вывод разницы начала и конца работы потоков
print(f'Работа потоков заняла: {time2_res} сек.')
