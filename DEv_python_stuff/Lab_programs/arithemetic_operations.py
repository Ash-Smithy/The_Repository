a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
flag = 0
while(flag!=1):
    choice = int(input("1.) for addition \n2.) for subtraction \n3.) for multiplication \n4.) for division \n5.)to quit \n:::"))
    if(choice == 1):
        print("the addition of the numbers is : ",a+b)
    elif(choice == 2):
        print("The subtraction of the numbers is : ",a-b)
    elif(choice == 3):
        print("The multiplication of the numbers is : ",a*b)
    elif(choice == 4):
        print("The division of the numbers is : ",a/b)
    elif(choice == 5):
        flag = 1
    else:
        print("invalid input")
