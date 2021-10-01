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
    del num[:]
    print("The entire list is now deleted after using del num[:]",num)
    print("creating another list and now adding elements in between instead of the end")
    list1 = [1,9,11,13,15]
    list1[1] = [3,5,7]
    print(list1)
    print(list1[1])
    print(list1[1][1])

def nested_list():
    list1 = [1,'a','abc',[3,5,7],8.9]
    i = 0
    while(i<len(list1)):
        print("List1[",i,"] = ",list1[i])
        i+=1
def cloning_list():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    list2 = list1
    print("list1 = ",list1)
    print("list2 = ",list2)
    list3 = list1[2:6]
    print("list3 = ",list3)
def del_items_using_empty_list():
    l1 = ['p','r','o','g','r','a','m']
    l1[2:5] = []
    print(l1)

