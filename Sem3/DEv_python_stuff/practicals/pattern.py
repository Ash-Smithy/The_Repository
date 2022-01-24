#program to demonstrate pattern using nested loops
limit = int(input("Enter the limit of the pattern"))
for i in range(1,limit+1):
    for j in range(1,i+1):
        print("*",end = ' ')
    print("\n")
