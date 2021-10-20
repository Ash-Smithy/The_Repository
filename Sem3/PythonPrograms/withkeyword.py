with open("hello.txt","r") as file:
    for line in file:
        print(line)
print("Is the file closed",file.closed)