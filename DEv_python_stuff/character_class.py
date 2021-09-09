import re
pattern = r"[aeiou]"
if re.search(pattern, "clue"):
    print("matche clue")
else:
    print("not found")
if re.search(r"[^aeiou]", "bcdfg"):
    print("match bcdfg")
else:
    print("not found")
