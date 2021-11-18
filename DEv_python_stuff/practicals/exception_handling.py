class invalidAge(Exception):
    def display(self):
        print("sorry! Age cannot be below 18 and you can't vote")
class invalidName(Exception):
    def display(self):
        print("Please enter a valid name ")
try:
    name = input("Enter the name : ")
    if len(name) == 0:
        raise invalidName
    age = int(input("Enter the age : "))
    if age < 18:
        raise invalidAge
except invalidName as n:
    n.display()
except invalidAge as e:
    e.display()
else:
    print(name, " congratulations you can vote!")
