import re
ahem="She sells sea shells on the sea shore"
patt='sea'
rep='ocean'
new_string=re.sub(patt,rep,ahem)
print(new_string)

pattern="[a-zA-Z]"
matches = re.findall(pattern,"VDI 20104, Maruthi Suzuki Cars in India")
print(matches)