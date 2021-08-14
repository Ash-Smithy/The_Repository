list_to_search = [5,6,8,9,10]
n=5
flag = 0
for i in list_to_search:
    print("\t",i,"\t")

x = int(input("\nEnter the value to search - "))

print("\nFirst sorting the list/array \n")

print(list_to_search,"\n")
lb = 0
ub = n

while(flag!=1):
    mb = lb+((ub-lb)/2)
    if(ub<lb):
        print("\nthe element does not exist in the array\n")
        flag = 1
    elif(list_to_search[mb]<x):
        lb = mb+1
    elif(list_to_search[mb]>x):
        ub = mb-1
    elif(list_to_search[mb]==x):
        print("\nThe element is found at position ",mb+1)
        flag = 1    
