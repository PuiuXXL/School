import math

class Geometric_Form:
    def getArea(self):
        pass
    def getPerimeter(self):
        pass

class Rectangle(Geometric_Form):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def getArea(self):
        return self.height * self.width
    def getPerimeter(self):
        return 2 * self.width + 2 * self.height

class Circle(Geometric_Form):
    def __init__(self,radius):
        self.radius = radius
    def getArea(self):
        return math.pi * self.radius * self.radius
    def getPerimeter(self):
        return 2 * math.pi * self.radius

rectangle = Rectangle(2,2)
circle = Circle(1)
print(rectangle.getArea())
print(circle.getArea())