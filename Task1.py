"""
Задача №6
📌 Изменяем класс прямоугольника.
📌 Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.
"""

# Решение взято ваше. Разбор решения посмотрел.

class ValidateSize:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name.capitalize()} cannot be negative.")
        instance.__dict__[self.name] = value


class Rectangle:
    width = ValidateSize('_width')
    height = ValidateSize('_height')

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)


rectangle = Rectangle(4, 5)
print("Width:", rectangle.width)
print("Height:", rectangle.height)
print("Area:", rectangle.area)
print("Perimeter:", rectangle.perimeter)

rectangle.width = 6
rectangle.height = 8
print("Updated Width:", rectangle.width)
print("Updated Height:", rectangle.height)
print("Updated Area:", rectangle.area)
print("Updated Perimeter:", rectangle.perimeter)

try:
    rectangle.width = -2
except ValueError as e:
    print("Error:", e)

try:
    rectangle.height = -3
except ValueError as e:
    print("Error:", e)
