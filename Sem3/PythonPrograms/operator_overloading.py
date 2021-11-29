#overload + operator on complex object
from typing import ByteString


class Complex:
    def __init__(self):
        self.real=0
        self.imag=0
    def setvalue(self,a,b):
        self.real=a
        self.imag=b
    def __add__(self,c):
        Temp=Complex()
        Temp.real=self.real+c.real
        Temp.imag=self.imag+c.imag
        return Temp
    def display(self):
        print("(",self.real,"+",self.imag,"i)")
class real:
    def __init__(self):
        self.real = 0
        self.imag = 0
    def setvalue(self,a,b):
        self.real = a
        self.imag = b
    
c1=Complex()
c1.setvalue(1,2)
c2=Complex()
c2.setvalue(3,4)
c3=c1+c2 #as c1 and c2 are complex type, c3 will automatically be complex type
c3.display()
c4 = real()
c4.setvalue(7,8)
c5 = c1+c4
c5.display()
