from tkinter import *
root = Tk()
def print_selection():
    if(var1.get()==1) & (var2.get()==0):
        l1.config(text = 'python')
    elif(var1.get()==0) & (var2.get()==1):
        l1.config(text = 'java')
    elif (var1.get() == 1) & (var2.get() == 1):
        l1.config(text = 'python and java')
    else:
        l1.config(text = 'Nothing!!')
root.geometry('400x600')
root.title('baaaah check box')
frame1 = Frame(root)
frame1.pack()
var1 = IntVar()
var2= IntVar()
chkbtn1 = Checkbutton(frame1,text = 'python',variable = var1,onvalue=1,offvalue=0,command = print_selection)
chkbtn2 = Checkbutton(frame1,text = 'Java',variable = var2,onvalue=1,offvalue=0,command = print_selection)
chkbtn1.pack(side = 'left')
chkbtn2.pack(side = 'right')
l1 = Label(frame1,text='empty',bg = 'white',width = 20)
l1.pack(side = 'bottom')
root.mainloop()