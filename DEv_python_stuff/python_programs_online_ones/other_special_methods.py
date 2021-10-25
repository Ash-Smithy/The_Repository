#the other special methods
#__repr__()
#__cmp__()
#__len__()

class ABC():
    def __init__(self,name,var):
        self.name = name
        self.var = var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var - obj.var
obj = ABC("abcdef",10)
print("the value stored in object is : ",repr(obj))
print("The length of name stored in object is : ",len(obj))
obj1 = ABC("ghijkl",1)
val = obj.__cmp__(obj1)
if val == 0:
    print("Both values are equal")
elif val == -1:
    print("First value is less than second")
else:
    print("The second value is less than the first one")
    