string1 = input("enter a string")
freq_dict = {}
for character in string1:
    if character in freq_dict:
       freq_dict[character] += 1
    else:
       freq_dict[character] = 1  
for character,freq in freq_dict.items():
    print("character : ",character , " freq : ",freq)
