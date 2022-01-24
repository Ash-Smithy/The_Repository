class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print('name ',self.name)
        print('age : ',self.age)
class Teacher(Person):
    def __init__(self,name,age,w_exp,area):
        Person.__init__(self,name,age)
        self.w_exp = w_exp
        self.area = area
    def display_data(self):
        print("Experience",self.w_exp)
        print("Area: ",self.area)
class Student(Person):
    def __init__(self,name,age,course, marks):
        Person.__init__(self,name,age)
        self.course = course
        self.marks = marks
    def display_det(self):
        print("course : ",self.course)
        print("marks : ",self.marks)
print("the student and teacher details are :: \n")
s = Student('Ash',19,'CS',97)
t = Teacher('John',43,8,'Data mining')
s.display()
s.display_det()
t.display()
t.display_data()
print("T is a teacher", isinstance(t,Teacher))
print("Teacher is a subclass", issubclass(Teacher,Person))
