def line_byline():
    file = open("1.txt","r")
    print("First line : ",file.readline())
    print("second line : ",file.readline())
    print("third line : ",file.readline())
def all_atonce():
    file = open("1.txt","r")
    print(file.read())
    file.close()
def list_method():
    file = open("1.txt","r")
    print(list(file))
    file.close()
def with_keyword():
    with open("1.txt","r") as file:
        for line in file:
            print(line)
    print("Is the file closed : ",file.closed)

file = open("1.txt","r")
print(file.read())
file.close()