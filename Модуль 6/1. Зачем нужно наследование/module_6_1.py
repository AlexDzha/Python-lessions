"""
2 класса родителя: Animal, Plant
"""
class Animal:
    """
    Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный),
    name - индивидуальное название каждого животного.
    """
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
class Plant:
    """
    Для класса Plant атрибут edible = False(съедобность),
    name - индивидуальное название каждого растения

    """
    edible = False
    def __init__(self, name):
        self.name = name
"""
4 класса наследника:
Mammal, Predator для Animal.
Flower, Fruit для Plant.
"""
# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
# Мы по возможности должны избегать лишнего дублирования кода.
# Запишем их в класс родитель Animal.
class Mammal(Animal):
    pass
class Predator(Animal):
    pass
class Flower(Plant):
    pass
class Fruit(Plant):
    edible = True
# Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.