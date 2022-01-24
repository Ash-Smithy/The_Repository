#program to demonstrate local and global variable
num1 = 10 #global variable
print("Global variable num1 : ",num1)
def func1(num2):
    print('In function local variable num2 : ',num2)
    num3 = 30
    print("In function local variable num3 : ",num3)
func1(20)
print("global variable num1 : ",num1)
print("Local variable num3 defined in function ",num3)
print('local variable num2 outside function ',num2)
