#ultimate string program
#slice
str1 = 'PYTHON'
print('printing the string in reverse : ',str1[::-1])
print("printing the string till the 6th index : ",str1[:6])
#the order function
print("the order function : ",ord('A'))

#string replacement using RE
import re
ahem = 'She sells sea shells on the sea shore'
pattern1 = 'sea'
replacement = 'ocean'
new_string = re.sub(pattern1,replacement,ahem)
print("the new string is : ",new_string)
pattern = r'[a-zA-Z]+ \d'
match = re.findall(pattern,'LXI 2013, VXI 2015,VDI 20104, Maruthi Suzuki Cars in India')
for x in match:
    print("Match found at : ",x.start())
    print("match found at : ",x.end())
    print("match found at : ",x.span())
pattern2 = r'[aeiou]'
if re.search(pattern2,'aeiou'):
    print("no nanananananana")
else:
    re.search(pattern1)

#some string functions
str3 = 'is this your bag?'

