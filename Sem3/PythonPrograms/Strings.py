#all about strings
def string_example1():
    message = "Hello"
    index = 0
    for i in message:
        print("Message(",index,")",i)
        index = index + 1
def String_ex2():
    str1 = "Hello"
    str2 = "World"
    str3 = str1+str2
    print(str3)
def String_ex3():
    str1 = "Hello"
    str2 = "World"
    str2+=str1
    print(str2)
string_example1()
String_ex2()
String_ex3()

