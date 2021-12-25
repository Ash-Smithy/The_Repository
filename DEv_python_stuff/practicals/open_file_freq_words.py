file1 = open('1.txt','r')
counts = dict()
for line in file1:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1
print(counts)
file1.close()
