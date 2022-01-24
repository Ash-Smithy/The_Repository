x = lambda num : 1 if num <=1 else num*x(num-1)
number = int(input("enter a number : "))
print("%d != %d "%(number, x(number)))
