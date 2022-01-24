#abstract classes 

#operator overloading
def op_over():
    class complex:
        def __init__(self):
            self.real = 0
            self.imag = 0
        def setvalue(self,a,b):
            self.real = a
            self.imag = b
        def __add__(self,c):
            Temp = complex()
            Temp.real = self.real + c.real
            Temp.imag = self.imag + c.imag
            return Temp
        def display(self):
            print(" ",self.real," + ",self.imag,"i ")
    c1 = complex()
    c1.setvalue(6,7)
    c2 = complex()
    c2.setvalue(8,9)
    c3 = c1+c2
    c3.display()    
#exception handling
def exception_handling():
    class InvalidAge(Exception):
        def display(self):
            print("sorry! Age less than 18")
    class InvalidName(Exception):
        def display(self):
            print("Enter a valid name")
    try:
        name = input("Enter a name : ")
        if len(name)==0:
            raise InvalidName
        age = int(input("enter your age : "))
        if age < 18:
            raise InvalidAge
    except InvalidAge as n:
        n.display()
    except InvalidName as n:
        n.display()
    else:
        print(name, " you are eligible to vote!@")

#function arguments
#positional arguments
def f1(x,y):
    sum = x+y
    print("the sum is : ",sum)
f1(5,2)
#keyword arguments
def f2(item,price):
    print(item," priced : ",price)
f2(item = 'book',price = 3499)
#default arguments
def f3(item,price=1111):
    print(item," priced : ",price)
f3(item = 'book')
#variable length arguemnts
def f4(*x):
    for i in x:
        print(i,end = ' ')
f4(1,2,3,4,5,6)
#keyword variable length argument
def f5(**x):
    for i,j in x.items():
        print(i," ",j)
f5(a=1,b=2,c=3)
f5(item = 'bob',price =4444)
def rec_fact(n):
    if n <= 1:
        return 1
    else:
        return n*rec_fact(n-1)
print(rec_fact(5))
def rec_fib(n):
    if n<=1:
        return 1
    else:
        return (rec_fib(n-1)+rec_fib(n-2))
for i in range(5):
    print(rec_fib(i))

#lambda function also known as anonymous functions
f = lambda n:n if n<=1 else n*f(n-1)
print(f(5))
#regular expressions
import re
patt = r"Dev"
string1 = "Devansh Dev 354"
x = re.search(patt,string1)
if x:
    print('match found')
else:
    print('match not found')

y = re.match(patt,string1)
print(y.group(0))

z = re.findall(patt,string1)
print(z)
print(re.split(patt,string1))