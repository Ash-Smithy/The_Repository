import re
string1 = "She sells sea shells on the sea shore"
string2 = 'ocean'
x = re.sub('sea',string2,string1)
print(x)
#findall
pattern=r'[a-zA-z]'
y = re.findall(pattern,'well this is weird')
print(y)