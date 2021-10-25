class ABC():
    class_var=0
    def __init__(self,var):
        ABC.class_var+=1
        self.var=var
        print("The object value is: ",var)
        print("The value of class variable is: ",ABC.class_var)
    def __del(self):
        ABC.class_var -=1
        print("Object with value %d is going out of scope" %self.var)
obj1 = ABC(10)
obj2 = ABC(20)
obj3 = ABC(30)
del obj1
del obj2
del obj3
