#Program that converts a list of def axii_val(x): chracters into ASCII valoues return ord(x) using map()
char_list=['a','b','c','d','e','f','g','h','i','j']
print("Character list: ",char_list)
new_list=list(map(ascii_val,char_list))
print(list(zip(char_list,new_list)))