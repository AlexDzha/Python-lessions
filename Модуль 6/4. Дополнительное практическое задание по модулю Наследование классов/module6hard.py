class Figure:
    sides_count = 0

    def __init__(self, color: list, *sides: int):
        self.__color = color if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides = sides if len(sides) == self.sides_count else [1] * self.sides_count
        self.filled = False

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        return all(0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if r < 0 or g < 0 or b < 0:
            raise ValueError("Цвета не могут быть отрицательными.")
        elif self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]


    def __is_valid_sides(self, *sides):
        for side in sides:
            if type(side) != int or side <= 0:
                return False
        return len(sides) == len(self.__sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color: list, radius: int):
        super().__init__(color, radius)
        self.__radius = radius
    def get_square(self):
        return (self.__radius ** 2) * 3.14

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list, side_length: int):
        super().__init__(color, *[side_length] * 12)
        self.set_sides(*[side_length] * 12)

    def get_volume(self):
        return self.get_sides()[0] ** 3

# Код для проверки:
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
