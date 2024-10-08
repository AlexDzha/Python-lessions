# Имеющиеся данные:
class House: # Создаем класс
    def __init__(self, name, number_of_floors):  # добавиляем атрибуты
        self.name = name # название
        self.number_of_floors = number_of_floors #кол-во этажей
    # Добавляем спец. методы
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    """
    Дополняем Класс House:    
    1. Для сравнения количества этажей двух объектов класса House, 
    можно также предусмотреть действие, что other является числом:
    """
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(self,int):
            return self.number_of_dloors == other

    """
    2. Метод __lt__ : этот метод определяет поведение оператора "меньше чем" <. 
    Он сравнивает текущий объект с другим объектом:
    """
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    """
    3. Метод __le__: метод определяет поведение оператора "меньше или равно" <=. 
    Он использует методы __eq__ и __lt__:
    """
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    """
    4. Метод __gt__: определяет поведение оператора "больше чем" >. Он использует метод __le__. 
    Метод возвращает True, если текущий объект не меньше или равен other (используя __le__), что эквивалентно тому, что он больше.
    """
    def __gt__(self, other):
        return not self.__le__(other)

    """
    5. Метод __ge__: Этот метод определяет поведение оператора "больше или равно" >=. 
    Он использует метод __lt__. Метод возвращает True, если текущий объект не меньше other (используя __lt__), 
    что эквивалентно тому, что он больше или равен.
    """
    def __ge__(self, other):
        return not self.__lt__(other)


    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    """
    6.Метод __add__ , также можно дополнить вариантом, когда value(other) 
    является объектом класса House:
    """
    def __add__(self, value): # h1 = h1 + 10 или h1 = h1 + h2
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        return self

    """
    7. Методы __iadd__  и __radd__ не обязательно описывать заново, 
    достаточно вернуть значение вызова __add__:
    """
    def __radd__(self, other):
        return self.__add__(other)
    # h2 = 10 + h2 (метод вызывается, когда объект находится справа от оператора +, и левый оператор не поддерживает операцию сложения с ним)
    def __iadd__(self, other: int):
        return self.__add__(other) # h1 += 10 (метод вызывается, когда используется оператор +=)


# Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
