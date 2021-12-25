n = int(input("enter a number : "))
a = []
while(n>0):
    dig = n%2
    a.append(dig)
    n = n//2
a.reverse()
print("Binary Equivalent is : ")
for i in a:
    print(i,end = " ")
    