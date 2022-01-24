#hasattr(obj,name)
#getattr(obj,name[,default])
#setattr(obj,name,value)
#delattt(obj,name)
class ABC():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is : ",self.var)
obj = ABC(10)
obj.display()
print("Ceck if the object has attribute : ",hasattr(obj,'var'))
getattr(obj,'var')
setattr(obj,'var',50)
print("after setting value, var is : ",obj.var)
setattr(obj,'count',10)
print("the new variable count is created and its value is : ",obj.count)
print("after creating new attribute value, var is : ",obj.var)
delattr(obj,'var')

print("After deleting the attribute, var is : ",obj.var)
#__dict__
#__doc__
#__name__
#__module__
#__bases__
class ABCD():
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
        