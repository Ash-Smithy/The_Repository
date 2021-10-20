def prog1():
    def ascii_val(x):
        return ord(x)
    char_list = ['a','b','c','d','e','f','g','h','i','j']
    print("character list : ",char_list)
    new_list = list(map(ascii_val,char_list))
    print(list(zip(char_list,new_list)))

def linear_search():
    num_list= [56,78,23,10,11,34,22]
    num = int(input("enter the value to be searched"))
    i = 0
    flag = False
    while i < len(num_list):
        if num == num_list[i]:
            flag = True
        i+=1
    if(flag):
        print(num," found at ",i," location")
    else:
        print(num," not found")

def prog3():
    num_list = [1,2,3,4,5,6,5,4,3,2,1]
    num = int(input("Enter the value to be searched : "))
    i = 0
    count = 0
    while i<len(num_list):
        if num == num_list[i]:
            print(num, " found at location ",i)
            count+=1
        i+=1
    print(num," appears ",count," times in the list ")
def prog4():
    num_list = [1,2,3,4,5,6,7,6,5,4]
    print("original list ",num_list)
    i=0
    while i < len(num_list):
        num = num_list[i]
        for j in range(i+1,len(num_list)):
            val = num_list[j]
            if val == num:
                num_list.pop(j)
        i+=1
    print("list after removing the duplicate values : ",num_list)
prog4()
