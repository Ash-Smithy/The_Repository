class Student:
    def name(self):
        print('Name..')
class Acad_Pref(Student):
    def Acad_score(self):
        print("Acad score.... 90 percent and above")
class ECA(Student):
    def ECA_score(self):
        print('ECA score .. 60% and above')
class Result(Acad_Pref,ECA):
    def Eligibility(self):
        self.name()
        self.Acad_score()
        self.ECA_score()
R=Result()
R.Eligibility()