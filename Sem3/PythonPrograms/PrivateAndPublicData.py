#Public variables declared in class are public by defaul, using the dot operator
#Private variables are declared with __ at the beginning

class ABC:
    def __init__(self,var1,var2):
        self.var1=var1
        self.__var2=var2
    def display(self):
        print("Value of var1: ",self.var1)
        print("Value of var2: ",self.__var2)
obj=ABC(10,20)
obj.display()
print("Value of var1: ",obj.var1)
print("Value of var2: ",obj.__var2)
