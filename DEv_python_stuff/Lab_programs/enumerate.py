def enum_method():
    num = [1,2,3,4,5]
    for index,i in enumerate(num):
        print(i,"in at index : ",index)
def range_method():
    l1 = [1,2,3,4,5,6,7,8,9,10]
    for i in range(len(l1)):
        print("index : ",i)
def iterator_method():
    l1 = [1,2,3,4,5,6,7,8,9,10]
    it = iter(l1)
    for i in range(len(l1)):
        print("Element at index ",i," is : ",next(it))
