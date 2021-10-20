filename = input("Enter the file name : ")
with open(filename) as file1:
    text = file1.read()
    letter = input("Enter the character to be searched : ")
    c = 0
    for char in text:
        if char == letter:
            c+=1
print(letter, " appears ",c," time(s) in a file")



