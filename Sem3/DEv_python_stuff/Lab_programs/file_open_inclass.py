def write_prog():
    file = open("1.txt","w")
    print("Name of the file : ",file.name)
    print("File is closed : ",file.closed)
    print("Access mode : ",file.mode)
    print("File is being closed . . . .")
    file.write("Hello, all, welcome to Python programming")
    file.close()
def writelines_prog():
    file2 = open("1.txt","a")
    file2.writelines(["hellllllo","world","this is weird"])
    print("Data written to file ... ")
def read_prog():
    file = open("1.txt","r")
    print(file.read(10))
    file.closed()
read_prog()