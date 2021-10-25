#clases and objects
class ABC:
    __var = 10
    def __init__(self,val): #parameterized constructor 
        print("inside class method")
        self.val= val
    def display(self):
        print(self.__var)
        print("nani!?")
obj = ABC(100)
print(obj.val)
print(obj.var)
obj.display()
obj2 = ABC()
print(obj.val)