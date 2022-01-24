#inheritance
#single inheritance 
def single_inheritance():
    class Base:
        def __init__(self,name):
            self.name = name
    class Derived(Base):
        def __init__(self,name,age):
            self.age = age
            Base.__init__(self,name)
        def display(self):
            print("Name : ",self.name) 
            print("Age  : ",self.age)
    object1 = Derived('Jacob',19)
    object1.display()
single_inheritance()
#multiple inheritance 
def multiple_inheritance():
    class Base1:
        def __init__(self,name):
            self.name = name
    class Base2:
        def __init__(self,age):
            self.age = age
    class Derived(Base1,Base2):
        def __init__(self,department,name,age):
            self.department = department
            Base1.__init__(self,name)
            Base2.__init__(self,age)
        def display_function(self):
            print("Name : ",self.name)
            print("Age  : ",self.age)
            print("Department : ",self.department)
    object1 = Derived('Computers',"jacob",19)
    object1.display_function()
#multilevel_inheritance
def multilevel_inheritance():
    class Level1:
        def __init__(self):
            print("well this is level 1!!")
    class Level2(Level1):
        def __init__(self):
            print("well this is level 2!!!")
    class Level3(Level2):
        def __init__(self):
            print("well this is level 3!!!!")
            Level1.__init__(self)
            Level2.__init__(self)
    object1 = Level3()
multilevel_inheritance()
