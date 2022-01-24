with open("2.txt","r") as file:
    line = file.readline()
    words = line.split()
    print(words)
    print(line)
    line2 = file.readline()
    print(line2)
    