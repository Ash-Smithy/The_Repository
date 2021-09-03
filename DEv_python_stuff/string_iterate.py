#iterating string
def using_for():
    str = "welcome to python"
    for i in str:
        print(i,end=" ")
def using_while():
    message = "Welcome to python"
    index = 0
    while(index < len(message)):
        letter = message[index]
        print(letter,end=" ")
        index += 1

using_while()
using_for()