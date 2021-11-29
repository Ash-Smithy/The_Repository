from tkinter import *
import tkinter.messagebox as messagebox
def do_something():
    messagebox.showinfo('Response','Thank you for clicking the button')
root=Tk()
f=Frame(root,height=350,width=350)
f.pack()
mybutton=Button(f,text="Klick",command="do_something")
quitbutton=Button(f,text="Quit",command=root.destroy)
mybutton.pack()
quitbutton.pack()
root.mainloop()
