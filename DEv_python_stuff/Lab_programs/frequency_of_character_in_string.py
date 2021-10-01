string = input("Enter some text ")
frequency_dict = {}
for character in string:
    if character in frequency_dict:
        frequency_dict[character] += 1
    else:
        frequency_dict[character] = 1
print("\n..............")
print("character\tfrequency")
print("\n..............")
for character, frequency in frequency_dict.items():
    print("%sc\t\t%5d"%(character,frequency))