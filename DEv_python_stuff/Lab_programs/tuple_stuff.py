def create_tuple():
    tup1 = []
    lim = int(input("Enter limit of elements for tuple : "))
    for i in range(lim):
        tup1.append(input("Enter element for tuple :: "))
    tup2 = tuple(tup1)
    print(type(tup2))

def inserting_element():
    tup2 = (1,2,3,4)
    tup3 = (5,6,7)
    tup4 = tup2+tup3
    print(tup4)
    print(type(tup4))

def deleting_element():
    tup2 = (1,2,3,4)
    tup3 = (5,6,7)
    tup4 = tup2+tup3[1]
    print(tup4)
    print(type(tup4))
