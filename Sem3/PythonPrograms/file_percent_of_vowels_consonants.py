#Program that reads data from a file and calculates the percentage of vowels & constants in the file
filename=input("Enter a filename: ")
with open(filename) as file1:
    text=file1.read()
    c_v=0
    c_con=0
    for char in text:
        if char in "aeiou":
            c_v+=1
        else:
            c_con+=1
print("Number of vowels: ",c_v)
print("Number of consonants: ",c_con)
print("Length of file: ",len(text))
print("Percentage of vowles in file: ",((c_v*100)/len(text)),"%")
print("Percentage of constants: ",((c_con*100)/len(text)),"%")