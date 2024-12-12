# Задание "Они все так похожи"
from math import pi, sqrt

class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled):
        self.__color = color if self.__is_valid_color(color[0], color[1], color[2]) else [0] * 3
        self.__sides = sides if self.__is_valid_sides(sides) else [1] * self.sides_count
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(list(new_sides)):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, *args):
        sides = list(args[1:])
        filled = True
        if isinstance(sides[-1], bool):
            filled = sides.pop()

        super().__init__(color = list(args[0]), sides = sides, filled = filled)
        self.__radius = args[0][0]/(2*pi)

    def get_square(self):
        return pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, *args):
        sides = list(args[1:])
        filled = True
        if isinstance(sides[-1], bool):
            filled = sides.pop()

        if len(sides) == 1:
            sides = sides * self.sides_count

        super().__init__(color=list(args[0]), sides=sides, filled=filled)

    def get_square(self):
        sides = self.get_sides()
        p = 0.5 * sides
        return sqrt(p * (p-sides[0]) * (p-sides[1]) * (p-sides[2]))

class Cube(Figure):
    sides_count = 12
    def __init__(self, *args):
        sides = list(args[1:])
        filled = True
        if isinstance(sides[-1], bool):
            filled = sides.pop()


        if len(sides) == 1:
            sides = sides * self.sides_count

        super().__init__(color=list(args[0]), sides=sides, filled=filled)

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