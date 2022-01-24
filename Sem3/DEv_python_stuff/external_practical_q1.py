#program to demonstrate class and object
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
s1 = Student('Jacob',19)
s1.display()
s2 = Student('Jonathan',18)
s2.display()
