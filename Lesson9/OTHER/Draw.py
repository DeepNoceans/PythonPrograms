#Draw a simple object hierarchy of a Shape class:
#  it will have an Ellipse and Polygon class inheriting
#  from the Shape class. Circle will inherit from Ellipse
#  and Rectangle and Triangle will inherit from Polygon.
#  Square will inherit from Rectangle.

#Shape ==> Ellipse & Polygon
#Ellipse ==> Circle
#Polygon ==> Rectanle & Square

import math

class Shape(object):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        rep = ""
        rep += f"Length: {self.length}"
        rep += f"Width: {self.width}"
        return rep

class Ellipse(Shape):

    def __init__(self, axis1, axis2):
        super().__init__(axis1, axis2)

  
    def Area(self):
        return math.pi * self.axis1 * self.axis2

    def Perimeter():
        print("Perimeter")


class Polygon(Shape):

    def Area():
        print("Area")

    def Perimeter():
        print("Perimeter")

class Circle(Ellipse):

    def __init__(self, radius):
        super().__init__(radius)
    
    def Area(self):
        return math.pi * self.radius ** 2

class Rectangle(Polygon):
    
    def Area(self, base, height):
        return self.base * self.height
    
    def Perimeter(self):
        return self.base * self.height

class Triangle(Polygon):

    def __init__(self, base, height, side1, side2):
        super().__init(base, height, side1, side2)

    def Area(self):
        return self.base * self.height * .5

    def Perimeter(self):
        return self.base + self.side1 + self.side2

class Square(Rectangle):

    def __init___(self, base):
        super().__init(base)

    def Area(self ):
        return self.base ** 2

    def Perimeter(self):
        return self.base * 4

