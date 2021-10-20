def sum(a,b):
    print("The sum of the numbers is : ",a+b)
def subtract(a,b):
    print("The subtraction of the numbers is : ",a-b)
def multiply(a,b):
    print("The product of the numbers is : ",a*b)
def division(a,b):
    print("The division of the numbers is : ",a/b)
def choice_selector(c,a,b):
    if(c == '+'):
        sum(a,b)
    elif(c == '-'):
        subtract(a,b)
    elif(c == '*'):
        multiply(a,b)
    elif(c == '/'):
        division(a,b)
    else:
        print("Invalid input")
