with open("text.txt","r") as file1:
    with open("2.txt","w") as file2:
        buf = file1.read(10)
        file2.write(buf)
print("file copied")
