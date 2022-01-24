files = open('1.txt','r')
string1 = files.read()
freq_dict = {}
for characters in string1:
    if characters in freq_dict:
        freq_dict[characters]+=1
    else:
        freq_dict[characters] = 1
for characters,freq in freq_dict.items():
    print(characters,'frequency', freq )