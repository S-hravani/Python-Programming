#.Write a python class named Rectangle constructed by a length and width and a method which will compute area of rectangle

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print("Area of rectangle  = ",self.length*self.width)

r1 = Rectangle(10,9)
r1.calculate_area()