class ABC():
    class_var = 0
    def __init__(self,var):
        ABC.class_var +=1
        self.var = var
        print("the object value is : ",var)
        print("the value of the class is : ",ABC.class_var)
obj1 = ABC(10)
obj2 = ABC(20)
obj3 = ABC(30)
