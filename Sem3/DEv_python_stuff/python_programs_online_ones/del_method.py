class ABC():
    class_var = 0 #class variable/ static variable
    def __init__(self,var): #parameterized constructor
        ABC.class_var += 1
        self.var = var
        print("the object value is : ",var)
        print("the value of the class variable is : ",ABC.class_var)
    def __del__(self):
        ABC.class_var -= 1
        print("the object with value %d is going out of scope "%self.var)
        print(ABC.class_var)
    __var2 = 1000
    def print_this(self):
        print(self.__var2)
    var3=1003
obj1 = ABC(10)
obj2 = ABC(20)
obj3 = ABC(30)
obj1.print_this()
print(obj1.var3)
del obj1
del obj2 
del obj3
