from tkinter import *
from tkinter import messagebox
root =Tk()
entry = Entry(root)
entry.pack()
def printMsg():
    messagebox.showinfo('Popup',entry.get())
button = Button(root,text = 'print content',command = printMsg)
button.pack()
root.mainloop()
