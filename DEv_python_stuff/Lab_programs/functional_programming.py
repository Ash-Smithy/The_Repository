def filter_method():
    def check(x):
        if((x%2==0) or (x%4==0)):
            return 1
    evens = list(filter(check,range(1,10)))
    print(evens)
def map_method():
    def add_2(x):
        x+=2
        return x
    n = [1,2,3,4,5]
    new_list = list(map(add_2,n))
    print("modified list is : ",new_list)

def reduce_method():
    import functools
    def add_1(x,y):
        return (x+y)
    l = [1,2,3,4,5]
    print("Sum of the values : ")
    print(functools.reduce(add_1,l))
