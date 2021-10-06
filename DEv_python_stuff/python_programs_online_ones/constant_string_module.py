#working with constants in string module
import string
#first way
def first():
    print(string.find(string.ascii_lowercase, 'g')!=-1)
#second way
def second():
    print('g' in string.ascii_lowercase)
#third way
def third():
    ch = 'g'
    print('a' <= ch <= 'z')
first()
second()
third()
