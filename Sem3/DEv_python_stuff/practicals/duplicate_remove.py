list1 = [11,3,2,5,3,2,33,7,8,9]    #creating the list
new_list = []   #creating an empty list
for i in list1:    
    if i not in new_list:
        new_list.append(i)
print('original : ',list1)
print("duplicates removed : ",new_list)
