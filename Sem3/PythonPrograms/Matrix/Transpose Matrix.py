x=[[12,7,0],[4,5,0],[3,8,0]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x)):
        result[j][i] = x[i][j]
for r in result:
    print(r)