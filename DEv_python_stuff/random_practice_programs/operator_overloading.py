#operator overloading
#addition operator
class mew:
    def __init__(self):
        self.real = 0
        self.imag = 0
    def set_value(self,imag,real):
        self.real = real
        self.imag = imag
    def __add__(self,c):
        Temp = mew()
        Temp.real = self.real + c.real
        Temp.imag = self.imag + c.imag
        return Temp
    def display(self):
        print(" ",self.real," + ",self.imag,"i ")
c1 = mew()
c1.set_value(5,6)
c2 = mew()
c2.set_value(7,8)
c3 = c1 + c2
c3.display()


