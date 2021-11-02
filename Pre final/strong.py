def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f
# function to check strong
def check_strong(n):
    number_copy = n
    strong_sum = 0
    while n:
        remainder = n%10
        strong_sum += fact(remainder)
        n //= 10
    return strong_sum == number_copy
# Reading number
number = int(input('Enter number: '))
# Making decision
if check_strong(number):
    print('%d is STRONG.' %(number))
else:
    print('%d is NOT STRONG.' %(number))
