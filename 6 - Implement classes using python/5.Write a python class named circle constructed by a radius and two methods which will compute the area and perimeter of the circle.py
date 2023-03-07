#Write a python class named circle constructed by a radius and two methods which will compute the area and perimeter of the circle

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area_of_circle(self):
        return 3.14*self.radius*self.radius

    def perimeter_of_circle(self):
        return 2*3.14*self.radius

obj = Circle(5)
print("area of circle = ",obj.area_of_circle())
print("Perimeter of circle = ",obj.perimeter_of_circle())
