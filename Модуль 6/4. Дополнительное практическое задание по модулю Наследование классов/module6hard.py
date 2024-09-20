class Figure:
    sides_count = 0
    def __init__(self, color: list, *sides: int, filled: bool = True):
        if len(sides) != self.sides_count:
            self.__sides = [1*self.sides_count]
        else:
            self.__sides = [i for i in sides]
        self.__color = [color]
        self.filled = filled
    def get_color(self):
        return list(self.__color)
    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Ошибка! Значения цветов RGB обозначаются в диапазоне от 0 до 255 включительно!")

    def __is_valid_sides(self, *sides):
        for side in sides:
            if type(side) == int and side > 0 and len(sides) == len(self.__sides):
                return True
            else:
                return False
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
class Circle(Figure):
    sides_count = 1
    def __radius(self):
        return self.__len__ ()/(2*3.14)

    def get_square(self):
        return (self.__radius() ** 2) * 3.14
class Triangle(Figure):
    sides_count = 3
    def get_square( self,a,c,d):
        p = (a+c+d)/2
        return (p*(p-a)*(p-d)*(p-c))**0.5


class Cube(Figure):
    sides_count = 12
    def set_side_lst(self):
        set_side_lst = []
        for element in range(self.sides_count):
            set_side_lst.append(self.side)
        self.__sides = set_side_lst
        return self.__sides
    def __init__(self, color, side_length):
        super().__init__([side_length] * 12, color)

    def get_volume(self):
        return self.get_sides()[0] ** 3


# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())