#Program that copies first 10 byes of a file into another
with open("file.txt","r") as file:
    with open("file2.txt","r") as file2:
        buf=file.read(10)
        file2.write(buf)
print("File copied")