def fibonacci_function():
    #program for printing fibonacci series using recursion
    n = int(input("enter the limit for the fibonacci series : "))
    def fib(n):
        if(n<2):
            return 1
        return (fib(n-1)+fib(n-2))
    for i in range(n):
        print("fibonacci (",i,") = ",fib(i))
def GCD_function():
    #program for GCD using recursion
    def gcd(x,y):
        rem = x%y
        if rem == 0:
            return y
        else:
            return gcd(y,rem)
    a = int(input("enter first no : "))
    b = int(input("enter second number : "))
    print("the GCD of the two numbers is : ",gcd(a,b))
def exponent_function():
    #exponent using recursion
    def exp(x,y):
        if(y==0):
            return 1
        else:
            return(x*exp(x,y-1))
    a = int(input("Enter no : "))
    b = int(input("enter the power : "))
    print("The result is : ",exp(a,b))
