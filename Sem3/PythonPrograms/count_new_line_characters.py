#program that counts the number of tabs,spaces and new line characters in a  file
filename=input("Enter a filename: ")
with open(filename) as file:
    text=file.read()
    c_t=c_sp=c_nl=0
    for char in text:
        if char=="\t":
            c_t+=1
        if char==" ":
            c_sp+=1
        if char=="\n":
            c_nl+=1
print("Tabls: ",c_t)
print("Spaces: ",c_sp)
print("New_Lines: ",c_nl)