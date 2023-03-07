#Write a python class which has two methods getstring and printstring getstring accept a string from user and printstring print in uppercase

class Cstring:
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter a string = ")

    def print_string(self):
        print(self.str1.upper())

str = Cstring()
str.get_string()
str.print_string()
