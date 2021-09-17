def pattern_match1():
    import re
    pattern = r"gr(ea)*t"
    if re.match(pattern, "great"):
        print("match ea")
    if re.match(pattern,"greaeaeaeat"):
        print("match found")
def pattern_match_group():
    import re
    pattern = r"Go(od) Go(in)g Py(th)on"
    match = re.match(pattern,"Good Going Python Good Going Python Good Going Python")
    if match:
        print(match.group())
        print(match.group(1))
        print(match.group(2))
        print(match.groups())
def named_groups():
    import re
    pattern = r"Go(?P<FIRST>od) Go(?:in)g Py(th)on"
    match = re.match(pattern, "Good Going Python Good Going Python Good Going Python")
    if match:
        print(match.group())
        print(match.group("FIRST"))
        print(match.group(2))
        print(match.groups())
def extract_email():
    import re
    pattern = r"[\w.-]+@[\w.-]+"
    match = re.search(pattern,"please send your feedback to info@oxford.com")
    if match:
        print("Email to : ",match.group())
    else:
        print("NO match")
flag = 0
while(flag !=1):
    choice = int(input("\nEnter choice :: \n1.)Pattern match ex 1\n2.) pattern match group \n3.)named groups \n4.)To extract email \n5.)to quit"))
    if(choice == 1):
        pattern_match1()
    elif(choice == 2):
        pattern_match_group()
    elif(choice == 3):
        named_groups()
    elif(choice == 4):
        extract_email()
    elif(choice == 5):
        print("Exit!!")
        flag = 1
    else:
        print("invalid Input!")
        print("exiting!")
        flag = 1