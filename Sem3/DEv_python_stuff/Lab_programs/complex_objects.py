class One:
    def set(self,var):
        self.var=var
    def get(self):
        return self.var
class Two:
    def __init__(self,var):
        self.o=One()
        self.o.set(var)
    def show(self):
        print("Number =",self.o.get())
T=Two(3300)
T.show()
