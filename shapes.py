from abc import ABC, abstractmethod


class Shapes(ABC):
    @abstractmethod
    def calculatePerimeter(self):
        pass

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def calculatePerimeter(self):
        self.perimeter = 2 * 3.14 * self.radius
        return self.perimeter

class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculatePerimeter(self):
        self.perimeter = 2 * (self.width + self.height)
        return self.perimeter
c

circle = Circle(5)
print("Circle Perimeter:", circle.calculatePerimeter())

rectangle = Rectangle(4, 6)
print("Rectangle Perimeter:", rectangle.calculatePerimeter())
