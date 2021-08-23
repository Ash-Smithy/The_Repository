#a function that calls itself to solve. It has two cases:
#Base case: problem is simple enough to be solved directly without recursion
#Recusive case: problem is divided into simple sub parts. 
#Recursion uses divide and conquer technique to solve problems

def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
print ("fact of 6 is: ",fact(6))