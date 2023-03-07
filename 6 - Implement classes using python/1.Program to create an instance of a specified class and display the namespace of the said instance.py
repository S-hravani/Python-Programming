#Program to create an instance of a specified class and display the namespace of the said instance (Class:student,Attributes: id,name,class name)

class Student:
    def __init__(self,id,name,class_name):
        self.id = id
        self.name = name
        self.class_name = class_name

s1 = Student("Shravani",2010022,"SYBTECH")
print(s1.__dict__)
