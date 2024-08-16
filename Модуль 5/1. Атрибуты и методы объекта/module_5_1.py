
class House: #создали класс

    def __init__(self, name, number_of_floors): #добавили атрибуты
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor): #создаем метод go_to с параметром new_floor
        if new_floor>self.number_of_floors or new_floor<1: #условие для несуществующего этажа
            print('"Такого этажа не существует"')
    # закоментированный (работающий) вариант вместо or отдельным условием
        # elif new_floor < 1:
        #      print('"Такого этажа не существует"')
        else: #условие для существующих этажей
             for i in range(1, new_floor + 1): # выводит значение начиная с 1 этажа заканчивая нужным этажом
                 print(i)



# Исходные данные: (можно добавить еще при желании)
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
# h3 = House('Родовое поместье', 3)
h1.go_to(5)
h2.go_to(10)
# h3.go_to(0)