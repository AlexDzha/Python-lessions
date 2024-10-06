from random import choice

# Даны 2 строки:
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, mode='w', encoding='UTF-8') as file:
            for item in data_set:
                file.write(f"{item}\n")
    return write_everything
# Данный код:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *word):
        self.words = word
    def __call__(self):
        word = choice(self.words)
        return word
first_ball = MysticBall("Мальдивы", "Греция", "Кипр", "Турция", "Бали", "Мальта", "Флорида", "Тайланд", "Барбадос", "Сейшелы")
print(first_ball())
print(first_ball())
print(first_ball())