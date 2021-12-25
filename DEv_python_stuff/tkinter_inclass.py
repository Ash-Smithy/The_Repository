from tkinter import *
import tkinter.messagebox as mb
def do_something():
    n = int(e1.get())
    product = 1 
    for i in range(1,n+1):
        product *= i
    mb.showinfo('result!',('Factorial of ',str(n),'is',str(product)))

root = Tk()
f = Frame(root,height = 350, width = 300)
label1 = Label(f,text = 'ENter number to find factorial of : ')
e1 = Entry(f,width=10)
label1.pack(side = 'left')
e1.pack(side = 'left')
myButton = Button(f, text = 'click me! ',command = do_something)
myButton.pack(side = 'left')
f.pack()
root.mainloop()
