from tkinter import *
import tkinter.messagebox as mb
root = Tk()
def do_something():
    n=int(e1.get())
    product=1
    for i in range(1,n+1):
        product=product*i
    mb.showinfo('Result',('Factorial of', str(n), 'is',str(product)))

f=Frame(root,height=350,width=300)
label1=Label(f,text="enter number to find the factorial")
e1=Entry(f,width=10)
label1.pack(side='right')
e1.pack(side='right')
mybutton=Button(f,text="Click Me", command=do_something)
mybutton.pack(side='right')
f.pack()
root.mainloop()