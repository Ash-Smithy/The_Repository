odds = set([x*2+1 for x in range(1,10)])
print("odd numbers : ",odds)
primes = set()
for i in range(2,20):
    j = 2
    flag = 0
    while j<i/2:
        if i%j==0:
            flag =1
        j+=1
    if flag == 0:
        primes.add(i)
print('Prime numbers : ',primes)
print("union : ",odds.union(primes))
print("intersection : ",odds.intersection(primes))
print("symmetric difference : ",odds.symmetric_difference(primes))
print("difference : ",odds.difference(primes))
