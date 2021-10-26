class ABC():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("Var is = ",self.var)
obj = ABC(10)
obj.display()
print("Check if object has attribute var: ",hasattr(obj,'var'))
getattr(obj,'var')
setattr(obj,'var',50)
print("After setting value, var is: ",obj.var)
setattr(obj,'count',10)
print("New variable count is created with value: ",obj.count)
delattr(obj,'var')
#print("After deleting the attribute, var is: ",obj.var)