num1 = int(input("Enter a number"))
flag = num1 
sum = 0
while flag > 0:
    rem = flag%10
    sum = sum+(rem**3)
    flag = flag//10
print(sum)
if sum == num1:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
