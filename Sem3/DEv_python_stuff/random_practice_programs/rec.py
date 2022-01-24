def functions_arguments():
    #types of arguments in python
    #positional argument
    def func1(name,age):
        print("Name : ",name)
        print("Age  : ",age)
    func1('Jacob',19)
    #keyword argument
    def func2(name,age):
        print("Name : ",name)
        print("Age  : ",age)
    func2(age = 19,name = "Jacob")
    #default argument
    def func3(name=' ',age=0):
        print("Name : ",name)
        print("Age  : ",age)
    func3('Jacob')
    #variable length arguments
    def func4(*b):
        for i in b:
            print(i,end = " ")
    func4(1,2,3,4,5,56,7)
    #variable length keyword arguments
    def func5(a=0,**b):
        for j,i in b.items():
            print('\n',j," = ",i)
    func5(a = 4,name = 'Jacob',sur = "Collier")

#recursions
def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
for i in range(1,10):
    print(fib(i))
def fact(n):
    if n<=1:
        return n
    else:
        return (n*fact(n-1))
print("Factorial of 5 is ",fact(5))
def exponent(n,p):
    if p == 1:
        return n
    elif p == 0:
        return 1
    else:
        return (n*exponent(n,p-1))
print(exponent(5,3))
def GCD(x,y):
    rem = x%y
    if rem == 0:
        return y
    else:
        return GCD(x,rem)
print("THe GCD is : ",GCD(25,5))

#regular expressions
import re
string1 = 'She sells sea shells on the sea shore 1,2,3,4,5,6,7,8,9,10'
pattern1 = r'[a-zA-Z]'
pattern2 = 'sells'
x = re.match(pattern2,string1)
if x:
    print("found")
else:
    print("not found")
y = re.search(pattern2,string1)
if y:
    print("match found")
else:
    print("match not found ")
z = re.findall("sea",string1)
print(z)
a = re.sub('sea','ocean',string1)
print(a)
b = re.split('sea',string1)
print(b)
c = re.match('S h e',string1,re.X)
if c:
    print("match found")
else:
    print("match not found")

class complex:
    def __init__(self):
        self.real = 0
        self.imag = 0
    def setvalue(self,real,imag):
        self.real = real
        self.imag = imag
    def __add__(self,c):
        Temp = complex()
        Temp.real = self.real + c.real
        Temp.imag = self.imag + c.imag
        return Temp
    def display(self):
        print(" ",self.real,' + ',self.imag,"i")
ob1 = complex()
ob2 = complex()
ob1.setvalue(5,6)
ob2.setvalue(6,7)
ob3 = ob1+ob2
ob3.display()

list1 = [1,2,3,4,5,6,7]
import functools 
def function1(a,b):
    sum = a+b
    print(a," + ",b," = ",sum)
    return sum
print(functools.reduce(function1,list1))
def func2(a):
    exponent = a**2 
    return exponent
list2 = [1,2,3,45,5]
y = map(func2,list2)
print(list(y))
def func3(n):
    if n%2 == 0:
        return n
    else:
        pass
list3 = [1,2,3,4,5,6,7,8,9]
print(list(filter(func3,list3)))
  