from tkinter import *
def display():
    x = var1.get()
    y = var2.get()
    str = ''
    if x == 1:
        str+='Java'
    if y == 2:
        str+='python'
    ans = Label(text='you learnt '+str,fg = 'blue')
    ans.place(x = 50, y = 150,width = 200,height = 20)
root = Tk()
f = Frame(root,height = 300,width = 350)
f.pack()
var1 = IntVar()
var2 = IntVar()
label = Label(f,text = "select the language !")
c1 = Checkbutton(f,text='Java',variable = var1,onvalue = 1,command = display)
c2 = Checkbutton(f,text='python',variable = var2,onvalue = 2,command = display)
c1.place(x = 50, y= 100)
c2.place(x = 200 , y = 100)
root.mainloop()