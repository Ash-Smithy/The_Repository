from tkinter import *
def popup_window():
    pop = Tk()
    pop.geometry('300x300')
    pop.title("Alert!!")
    label1 = Label(pop,text = """Well the warning was given to you but you dareth 
    not listen so now suffer the consequences!""").pack(side='top')
    def boom():
        pop.destroy()
        root.destroy()
    button1 = Button(pop, text = "Ok!",command = boom).pack(side='top')
    pop.mainloop()
    

root = Tk()
root.geometry('600x400')
def warned():
    popup_window()

btn = Button(root,text="Don't you dare click this button",command = warned).pack()
root.resizable(False,False)
root.mainloop()