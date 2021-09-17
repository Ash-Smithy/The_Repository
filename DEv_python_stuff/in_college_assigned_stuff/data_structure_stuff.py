def cre_mani_slice():
    A = [1,2,3,4,5]
    D = [1,"string",'2+3i', 4.2]
    print("printing two lists :: ",A,D)
    num = range(1,11) # another way to create a list using the range function
    print("List created using range : ",num)
    #slicing
    print("Element at 0th index : ",num[0])
    print("Element at 1st index : ",num[1])
    print("Slicing from 2nd index to 5th index : ",num[2:5])
    print("Slicing with stride/step as 2",num[::2])
    print("Slicing with starting index as 1 and stride as 3 : ",num[1::3])
    print("printing list in reverse order : ",num[::-1])
    #updating values in a list
    print("before changing values :: ",num)
    num[0] = 10
    num[0:2] = [2,3]
    print("after changing values :: ",num)
    #using append to add another value at the end
    num.append(10)
    print(num)
    #len function used to find the no of elements in the list 
    print("the number of elements in the list is : ",len(num))
    #deleting elements in a list using the del method
    print("list before deleting an element : ",num)
    del num[10]
    print("list after deleting 10th index element : ",num)
