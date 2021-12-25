from tkinter import *
def display():
    x = var.get()
    str = ""
    if x == 1 :
        str+="you selected yes"
    if x == 2 : 
        str+='you have selected no'
    ans = Label(text=str,fg = 'blue')
    ans.place(x=50,y=150,width = 200,height = 20)
root = Tk()
f = Frame(root,height = 300,width = 500)
f.pack()
var = IntVar()
r1 = Radiobutton(f,text = "yes",variable = var,value = 1, command = display)
r2 = Radiobutton(f,text = "no",variable = var,value = 2, command = display)
r1.place(x = 50,y = 100)
r2.place(x=200,y=100)
root.resizable(0,0)

root.mainloop()