#fibonacci series using recursion
def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
def function_call():
    for i in range(10):
        print(fib(i))
#fibonacci without using recursions
def regular():
    lim = int(input("Enter a limit for the series : "))
    ft = 0
    st = 1
    print(ft,"\n",st)
    for i in range(lim):
        nt = ft+st
        print(nt)
        ft,st = st,nt
#factorial of a number the regular way
def fact_regualr_way():
    num = int(input('enter number to find the factorial of : '))
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial * i
    print("the factorial of the number is : ",factorial)
#factorial of a number using recursion
def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)
num = int(input("enter a number to find the factorial of : "))
print(fact(num))