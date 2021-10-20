with open("file.txt","r") as file:
    line=file.readline()
    words=line.split()
    print(words)