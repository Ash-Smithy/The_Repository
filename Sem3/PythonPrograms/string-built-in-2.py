str3="Is this your bag?"
print(str3.rfind("is"))
print(str3.rindex("your",0,len(str3)))

message="JamesBond007"
print("name")
print(message.isalnum())
print(message.isalpha())
print(message.isdigit())
message3="ABC"
print(message3.islower())
print(message3.isspace())
print(message3.isupper())
message2="pyton is Oops Language"
print(message2.swapcase())
print(message2.title())


str1="haleo"
str2="World"
print(str2.join(str1))
print(str1.just(15))