def single_line_lambda_rec():
    rec_lamda = lambda n :n if n<=1 else rec_lamda(n-1)+rec_lamda(n-2)
    lim = int(input("enter the limit for the series : "))
    for i in range(lim):
        print(rec_lamda(i))

power = lambda n,p : 1 if p == 0 else n*power(n,p-1)
print("the power of the number 6 is ",power(6,2))