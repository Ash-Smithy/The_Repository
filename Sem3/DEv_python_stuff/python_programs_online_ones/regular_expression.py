#regular expressions are a powerful tool for various string manipulation
#these are domain specific language that is present as a library in most modern programming languages besides python
#these come under the re module which comes as a part of the standard library
#A regular expression is a special sequence of characters that help us to match or find strings in another string.
""" the match function matches a pattern of string at the beginning of the string only and has following stuff
    re.I case sensitive matching 
    re.M matches at the end of the line
    re.X ignores whitespace characters
    re.U Interprets letters according to UNicode character set """
"""The search function in the RE module search for anywhere in the string 
    its syntax is re.search(pattern, string, flag = 0)
    the syntax is similar to match() function. THe function searches for the first occurrence of pattern 
    within a string with optional flags."""
"""The sub() function in the re module can be used to searcg a pattern in the string and replace it with another pattern
    The syntax if the sub() function replaces all occurrences of the pattern in tstring with repl, 
    substituting all occurrences unless any max value is provided
    This method returns modified string."""
#example program 1
import re

string = "she sells sea shells on the sea shore"

pattern1 = "sea"
if re.match(pattern1 , string,re.IGNORECASE):
    print("Match found")
else:
    print(pattern1, " is not present in the string")

pattern2 = "she"
if re.match(pattern2, string):
    print("Match found")
else:
    print(pattern2, " is not present in the string")

pattern3 = "shore"
if re.search(pattern3, string):
    print("Match found")
else:
    print(pattern3, " not found in the string")

new_string = re.sub("sea","ocean", string)

print(new_string)
"""
    findall() function is used to search a string and returns a list of matches of the pattern in the string.
    If no match is found, then the returned list is empty
    THe syntax can be 
    matchList = re.findall(pattern, input_str,flag = 0)"""
pattern4 = r"[a-zA-Z]+ \d+"
matches = re.findall("[a-zA-Z]+ \d+", "LXI 2013, VXI 2015, VDI 20104, Maruti Suzuki Cars in India")
print(matches)
#more re match stuff
#finditer
matches1 = re.finditer(pattern4, "LXI 2013, VXI 2015, VDI 20104, Maruti Suzuki Cars in India")
for match in matches1:
    print("Match found at starting index  = ",match.start())
    print("Match found at ending index = ",match.end())
    print("Match foudn at starting and ending index = ",match.span())
