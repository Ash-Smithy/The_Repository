filename = input("Enter the file name : ")
with open(filename) as file:
    text = file.read()
    c_t = c_sp = c_nl = 0
    for char in text:
        if char == "\t":
            c_t += 1
        elif char == " ":
            c_sp +=1
        elif char == "\n":
            c_nl +=1
        else:
            continue
print("tabs = ",c_t)
print("spaces = ",c_sp)
print("new lines = ",c_nl)
 