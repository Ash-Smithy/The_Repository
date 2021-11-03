class B1(object):
    def __init__(self):
        super(B1,self).__init__()
        print("Base Class")
class B2(object):
    def __init__(self):
        super(B2,self).__init__()
        print("B2 class")
class Derived(B1,B2):
    def __init__(self):
        super(Derived,self).__init__()
        print("Derived class")
D=Derived()