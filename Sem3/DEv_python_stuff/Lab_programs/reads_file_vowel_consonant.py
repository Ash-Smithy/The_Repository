filename = input('Enter a filename : ')
with open(filename) as file:
    text = file.read()
    c_v= 0
    c_con = 0
    for char in text:
        if char in "aeiou":
            c_v+=1
        else:
            c_con+=1
print("number of vowels : ",c_v)
print("number of consonant = ",c_con)
print("lenght of file = ",len(text))
print("percentage of vowels in file : ",((c_v*100)/len(text)))
print("percentage of consonants in file : ",((c_con*100)/len(text)))