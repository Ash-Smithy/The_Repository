def nested():
    list1 = [1,'a','abc',[3,5,7],8.9]
    i = 0
    while(i<len(list1)):
        print("list1[",i,"] = ",list1[i])
        i+=1

def delete_in_list():
    l1 = ['p','r','o','g','r','a','m']
    print(l1)
    l1[2:5]=[]
    print(l1)

