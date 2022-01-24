def comprehension_method():
    cubes = [i**3 for i in range(10)]
    print(cubes)
def regular_method():
    cubes = []
    for i in range(10):
        cubes.append(i**3)
    print(cubes)
def another():
    list1 = ([x,y] for x in [10,20,30]
                   for y in [20,30,40] if x!=y)
    print(list1)
another()