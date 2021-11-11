class Person:
    def name(self):
        print("Name:")
class Teacher(Person):
    def Qualification(self):
        print("PhD is must")
class HoD(Teacher):
    def experience(self):
        print("Experience -> 15 years")
hod = HoD()
hod.name()
hod.Qualification()
hod.experience()