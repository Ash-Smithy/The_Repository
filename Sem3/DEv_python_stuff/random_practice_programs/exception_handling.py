#errors in python can be of two types
#syntax erros and exceptions
#errors are the problems in a program due to which they would stop execution 
#exceptions are raised when some internal events occur which changes the normal flow of the program

class Invalid_name(Exception):
    def err_display(self):
        print("Invalid name entered!")
class Invalid_age(Exception):
    def err_display(self):
        print("Age less than 18, not eligible ")
try:
    name = input("Enter name : ")
    if len(name) == 0:
        raise Invalid_name
    age = int(input("Enter your age : "))
    if age < 18:
        raise Invalid_age
except Invalid_name as n:
    n.err_display()
except Invalid_age as n:
    n.err_display()
else:
    print("you are eligible to vote!")
finally:
    print("this statement will be printed anyways!")