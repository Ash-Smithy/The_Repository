class Student:
    def __init__(self,name,rno,eng,sci,cs):
        self.name = name
        self.rno = rno
        self.eng = eng
        self.sci = sci
        self.cs = cs
    def display(self):
        print("name : ",self.name)
        print("rno : ",self.rno)
        print("total score = ",self.eng+self.sci+self.cs)

s1 = Student('John',5,89,87,97)
s1.display()
s2 = Student('Sarah',6,88,98,87)
s2.display()