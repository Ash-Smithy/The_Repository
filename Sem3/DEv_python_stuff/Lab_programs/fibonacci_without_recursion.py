def gen_fibonacci(n):
    a,b = 0,1
    while a < n:
        print(a,end = ' ')
        next_num = a + b
        a,b=b,next_num
max_term = int(input("enter the macimum terms for the series : "))
gen_fibonacci(max_term)
 