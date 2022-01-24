def attempt_1():
    number = int(input("Enter a number : "))
    total_sum = 0
    step = 1
    condition = True
    while condition:
        while number:
            total_sum += number%10
            number = number//10
        print("Step %d: sum =  %d"%(step,total_sum))
        number = total_sum
        total_sum = 0
        step+=1
        condition = number > 9
def my_attempt():
    num = int(input("enter a 2 or more digit number : "))
    sum = 0
    temp_num = num    
    condition = True
    while condition is True:
        for i in range(2):
            sum = sum+num%10
            num = num//10
        print("the sum of the digits is : ",sum)
        num = sum    
        sum = 0
        condition = num > 9
