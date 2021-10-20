#Program that opens a file and counts the number of times a chaaracter appears in the file.
filename=input("Enter a  filename: ")
with open(filename) as file:
    text=file.read()
    letter=input("Enter a character to be searcherd: ")
    c=0
    for char in text:
        if char==letter:
            c+=1
print(letter,"appears",c,"time(s) in a file")