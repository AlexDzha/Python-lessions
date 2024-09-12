"""
Horse - класс описывающий лошадь.
"""
class Horse:
    def __init__(self):
        self.x_distance = 0     # пройденный путь.
        self.sound = 'Frrr'     # звук, который издаёт лошадь.
        super().__init__()

    def run(self, dx):          # изменение дистанции
        self.x_distance += dx   # увеличивает x_distance на dx.

"""
Eagle - класс описывающий орла. 
"""
class Eagle:
    def __init__(self):
        self.y_distance = 0      #  высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл (отсылка)

    def fly(self, dy):           # изменение дистанции
        self.y_distance += dy    # увеличивает y_distance на dy.

"""
Pegasus - класс описывающий пегаса. 
Наследуется от Horse и Eagle в том же порядке.
"""
class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):      # dx и dy изменения дистанции
        super().run(dx)
        super().fly(dy)

    def get_pos(self):  # возвращает текущее положение пегаса (x_distance, y_distance)
        return self.x_distance, self.y_distance

    def voice(self):    # значение унаследованного атрибута sound.
        print(self.sound)

# Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()