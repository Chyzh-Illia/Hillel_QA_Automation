from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14159 * (self.__radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.__radius


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self):
        s = (self.__a + self.__b + self.__c) / 2
        return (s * (s - self.__a) * (s - self.__b) * (s - self.__c)) ** 0.5

    def perimeter(self):
        return self.__a + self.__b + self.__c


shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(3, 4, 5),
]

for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"  Площа: {shape.area():.2f}")
    print(f"  Периметр: {shape.perimeter():.2f}")
    print()