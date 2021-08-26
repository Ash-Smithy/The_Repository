def max(numbers):
    print("User defined function max....")
    large=-1
    for i in numbers:
        if i > large:
            large = i
        return large
numbers=[9,-1,4,2,7]
print(max(numbers))
print("Sum of the numbers is ",sum(numbers))