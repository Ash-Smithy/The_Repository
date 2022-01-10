#multiple Inheritance 
class Base():
    def one(self):
        print("This is Base Class")
class Base2():
    def two(self):
        print("This is Base2 class")
class Derived(Base,Base2):
    def three(self):
        print("This is derived class")
k=Derived()
k.one()
k.two()
k.three()