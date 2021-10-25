file = open("text.txt","r")
counts = dict()
for line in file: 
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1
print(counts)
