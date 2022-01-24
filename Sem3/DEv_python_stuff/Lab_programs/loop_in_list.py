#to find sum and mean of elements in a list of first n natural numbers 
list1 = range(1,11)
sum = 0
for i in list1:
    sum = sum + i
print("the sum is : ",sum)
print("the mean is : ",(sum/len(list1)))
