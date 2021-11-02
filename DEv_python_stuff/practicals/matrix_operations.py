X = [[1,2,3],[4,5,6],[7,8,9]]
Y = [[1,1,1],[2,2,2],[3,3,3]]
r = [[0,0,0],[0,0,0],[0,0,0]]
print("matrix 1 : ",X)
print("matrix 2 : ",Y)
#addition 
for i in range(len(X)):
    for j in range(len(X[0])):
        r[i][j]=X[i][j]+Y[i][j]
print("the addition of the matrices is : ",r)
#subtraction
for i in range(len(X)):
    for j in range(len(X[0])):
        r[i][j]=X[i][j]-Y[i][j]
print("the subtraction of the matrices is : ",r)
#multiplication
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            r[i][j] += X[i][k] * Y[k][j]  
print("the multiplication of the matrices is : ",r)
#transpose
for i in range(len(X)):
    for j in range(len(X[0])):
        r[i][j]=X[j][i]
print("the transpose of matrix 1  : ",r)
for i in range(len(X)):
    for j in range(len(X[0])):
        r[i][j]=Y[j][i]
print("the transpose of matrix 2 : ",r)
