class ABC():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("Var is= ",self.var)
    def add_2(self):
        self.var +=2
        self.display()
obj = ABC(10)
obj.add_2()