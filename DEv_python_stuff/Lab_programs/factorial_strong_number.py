def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
def check_strong_number(n):
    num_cpy = n
    strong_sum = 0
    while n:
        remainder = n%10
        strong_sum +=fact(remainder)
        n//=10
    return strong_sum == num_cpy
number = int(input("enter number : "))
if(check_strong_number(number)):
    print("%d is strong "%(number))
else:
    print("%d is not strong "%(number))
print("Anyways the factorial of the number is : ",fact(number))
