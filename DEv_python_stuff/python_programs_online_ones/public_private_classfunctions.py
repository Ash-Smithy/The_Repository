#accessing private class method outside the class
class ABC:
    def __init__(self,var1):
        self.__var1=var1
    def __display(self):
        print("From class method , Var = ",self.__var1)
obj1 = ABC(10)
obj1._ABC__display()
#calling a class method from another class method
class ABC():
    def __init__(self,var):
        self.var = var
    def display(self):
        print("var is : ",self.var)
    def add_2(self):
        self.display()
        self.var+=2
        self.display()
obj = ABC(10)
obj.add_2()