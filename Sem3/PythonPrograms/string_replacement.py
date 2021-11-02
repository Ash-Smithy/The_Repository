import re
ahem="She sells sea shells on the sea shore"
patt='sea'
rep='ocean'
new_string=re.sub(patt,rep,ahem)
print(new_string)

pattern=r"[a-zA-Z]+ \d"
matches = re.findall(pattern,"VDI 20104, Maruthi Suzuki Cars in India")
print(matches)

pattern2=r"[a-zA-Z}+ \d+"
matchas=re.finditer(pattern2,"LXI 2013, VXI 2015,VDI 20104, Maruthi Suzuki Cars in India")
for match in matchas:
    print("Match fount at: ", match.start())
    print("Match fount at: ", match.end())
    print("Match fount at: ", match.span())


pattern3=r"[aeiou]"
if re.search(pattern3,"aeiou"):
    print("No nananananana")
else:
    re.search(pattern)