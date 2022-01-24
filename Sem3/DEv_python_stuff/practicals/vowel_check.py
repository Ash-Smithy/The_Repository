import re
char1 = input("Enter a character : ")
x = re.match(r"[aeiou]",char1)
if x:
    print("the character is a vowel")
else:
    print("the character is not a vowel")
