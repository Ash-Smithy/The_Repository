def sir_one():
    odds = set([x*2+1 for x in range(1,10)])
    print(odds)
    primes = set()
    for i in range(2,20):
        j = 2
        flag = 0
        while j<i/2:
            if i%j==0:
                flag = 1
            j+=1
        if flag==0:
            primes.add(i)
    print(primes)
    print("union :",odds.union(primes))
    print("Intersection :",odds.intersection(primes))
    print("symmetric difference : ",odds.symmetric_difference(primes))
    print("difference : ",odds.difference(primes))

odds = set([x*2+1 for x in range(1,10)])
print(odds)
prime = set()
for i in range(1,20):
    n=2
    for n in range(2,i):
        if i % n == 0:
            break
    else:
        prime.add(i)
print(prime)
print("union :",odds.union(prime))
print("Intersection :",odds.intersection(prime))
print("symmetric difference : ",odds.symmetric_difference(prime))
print("difference : ",odds.difference(prime))