num1=10
print('Global variabble num1=',num1)
def func(num2):
    print('In function-local variable num2 is ',num2)
    num3=30
    print('In function-Local variable num3 is', num3)
func(20)
print('num1 again =',num1)
print('Outside function num3 is: ',num3)
