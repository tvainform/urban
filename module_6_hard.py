# Задание "Они все так похожи"
from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for i in [r,g,b]:
            if not isinstance(i, int) or i not in range(0, 256):
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        if len(args) == len(self.__sides):
            for i in args:
                if not isinstance(i, int):
                    return False
            return True
        return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):

        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, *args):
        super().__init__(sides = args[0][:self.sides_count], color = args[1], filled = True)
        self.__radius = args[0][0]/(2*pi)

    def get_square(self):
        return pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, *args):
        super().__init__(color = list(args[0]), sides = list(args[1][:self.sides_count]), filled = True)

    def get_square(self):
        sides = self.get_sides()
        p = 0.5 * (sum(sides))
        return sqrt(p * (p-sides[0]) * (p-sides[1]) * (p-sides[2]))

class Cube(Figure):
    sides_count = 12
    def __init__(self, *args):
        super().__init__(color = list(args[0]), sides = [args[1]] * self.sides_count, filled=True)

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