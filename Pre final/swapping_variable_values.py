def method1():
    a = int(input("Enter first number : "))
    b = int(input("enter second number : "))
    print("The first number is : ",a," The second number is : ",b)
    a,b=b,a
    print("After swapping : a = ",a," b = ",b)
def method2():
    a = int(input("Enter first number : "))
    b = int(input("enter second number : "))
    print("The first number is : ",a," The second number is : ",b)
    temp = a
    a = b
    b = temp
    print("After swapping : a = ",a," b = ",b)
choice = int(input("1 for without temp variable, 2 for with temp variable : "))
if choice == 1:
    method1()
elif choice == 2:
    method2()
else:
    print("invalid input")