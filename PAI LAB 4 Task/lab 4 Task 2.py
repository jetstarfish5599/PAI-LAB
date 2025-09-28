from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass




class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


#Use
rect = Rectangle(10, 5)
tri = Triangle(6, 4)
sq = Square(7)

print(f"Rectangle area: {rect.area()}")
print(f"Triangle area: {tri.area()}")
print(f"Square area: {sq.area()}")
