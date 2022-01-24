def prog1():
    import math
    # Reading temperature in Celsius
    radius = float(input('Enter radius of circle: '))
    # Calculating area and circumference
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    # Displaying output
    print('Area = %0.4f.' % (area))
    print('Circumference = %0.4f.' % (circumference))
def prog2():
    def generate_fibonacci(n):
        a, b = 0, 1
        while a < n:
    # Print number
           print(a, end=', ')
    # Calculate next term
        next_num = a + b
    # Set a = b & b = next_num
        a, b = b, next_num
    # Input
    max_term = int(input('Enter maximum term of Fibonacci series: '))
    # Function Call
    generate_fibonacci(max_term)
def prog3():
    # Sum of digit until it reduces to single digit
    # Reading number
    number = int(input("Enter number: "))
    # Finding sum
    total_sum = 0
    step = 1
    condition = True
    while condition:
        while number:
            total_sum += number%10
            number //= 10
        print("Step-%d Sum: %d" %(step, total_sum))
        number = total_sum
        total_sum = 0
        step += 1
        condition = number > 9
def prog4():
    def fact(n):
        f = 1
        for i in range(1,n+1):
            f *= i
        return f
    # function to check strong
    def check_strong(n):
        number_copy = n
        strong_sum = 0
        while n:
            remainder = n%10
            strong_sum += fact(remainder)
            n //= 10
        return strong_sum == number_copy
    # Reading number
    number = int(input('Enter number: '))
    # Making decision
    if check_strong(number):
        print('%d is STRONG.' %(number))
    else:
        print('%d is NOT STRONG.' %(number))
def prog5():
    sentence = input("Enter sentence: ")
    # Finding longest word
    longest = max(sentence.split(), key=len)
    # Displaying longest word
    print("Longest word is: ", longest)
    print("And its length is: ", len(longest))

def prog6():
    # Shortest word
    # Reading text from user
    text = input("Enter some text: ")
    # Finding longest word
    shortest = min(text.split(), key=len)
    # Displaying longest word
    print("Shortest word is: ", shortest)
    print("And its length is: ", len(shortest))
def prog7():
    # Frequency of each character in string Get string from user
    string = input("Enter some text: ")
    # Set frequency as empty dictionary
    frequency_dict = {}
    for character in string:
        if character in frequency_dict:
            frequency_dict[character] += 1
        else:
            frequency_dict[character] = 1
    # Displaying result
    print("\n--------------------------")
    print("Character\tFrequency")
    print("--------------------------")
    for character, frequency in frequency_dict.items():
        print("%5c\t\t%5d" %(character, frequency))
def prog8():
    string = input("Enter some text: ")
    # Set frequency as empty dictionary
    frequency_dict = {}
    for character in string:
        if character in frequency_dict:
            frequency_dict[character] += 1
        else:
            frequency_dict[character] = 1
    most_occurring = max(frequency_dict, key=frequency_dict.get)
    # Displaying result
    print("\nMost occuring character is: ", most_occurring)
    print("It is repeated %d times" %(frequency_dict[most_occurring]))
def prog9():
    string = input('Enter anything: ')
    if string == string[::-1]:
        print('PALINDROME') 
    else :
        print('NOT PALINDROME')
def prog10():
    x = lambda num : 1 if num <= 1 else num*x(num-1)
    number = int(input('Enter number: '))
    print('%d != %d' %(number, x(number)))
def prog11():
    dec = int(input("Enter a number:"))
    print("The decimal value of", dec, "is:")
    print(bin(dec), "in binary.")
    print(oct(dec), "in octal.")
    print(hex(dec), "in hexadecimal.")
def prog12():
    # This function adds two numbers
    def add(x, y):
        return x + y

    # This function subtracts two numbers
    def subtract(x, y):
        return x - y

    # This function multiplies two numbers
    def multiply(x, y):
        return x * y

    # This function divides two numbers
    def divide(x, y):
        return x / y
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    while True:
        choice = input("Enter choice(1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            
        next_calculation = input("next operation (yes/no): ")
        if next_calculation == "no":
            break
        else:
            print("Invalid Input")
def prog13():
    X = [[12,7,3],[4 ,5,6],[7 ,8,9]]
    Y = [[5,8,1],[6,7,3],[4,5,9]]
    result = [[0,0,0],[0,0,0],[0,0,0]]
    # iterate through rows
    for i in range(len(X)):
    # iterate through columns
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]
    for r in result:
        print(r)
 
def prog14():
    X = [[12,7,3],[4 ,5,6],[7 ,8,9]]
    Y = [[5,8,1],[6,7,3],[4,5,9]]
    result = [[0,0,0],[0,0,0],[0,0,0]]
    # iterate through rows
    for i in range(len(X)):
    # iterate through columns
        for j in range(len(X[0])):
            result[i][j] = X[i][j] - Y[i][j]
    for r in result:
        print(r)
def prog15():
    # Program to multiply two matrices using nested loops
    # 3x3 matrix
    X = [[12,7,3],[4 ,5,6],[7 ,8,9]]
    # 3x4 matrix
    Y = [[5,8,1,2],    [6,7,3,0],    [4,5,9,1]]
    # result is 3x4
    result = [[0,0,0,0],         [0,0,0,0],         [0,0,0,0]]
    # iterate through rows of X
    for i in range(len(X)):
    # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    for r in result:
        print(r)
def prog16():
    # Program to transpose a matrix using a nested loop
    X = [[12,7],    [4 ,5],
        [3 ,8]]

    result = [[0,0,0],
            [0,0,0]]
    # iterate through rows
    for i in range(len(X)):
        # iterate through columns
        for j in range(len(X[0])):
            result[j][i] = X[i][j]
    for r in result:
        print(r)