from tkinter import *
root=Tk()
f=Frame(root,height=300,width=350)
f.pack()
var=IntVar()
label=Label(f,text='Select the language')
c1=Checkbutton(f,text="Java",variable=var1,value=1,command=display)
c2=Checkbutton(f,text="Python",variable=var2,value=2,command=display)
c1.place(x=50,y=100)
c2.place(x=200,y=100)
root.mainloop()
def display():
	x=var1.get()
	y=var2.get()
	str=''
	if x==1:
		str+='Java'
	if y==2:
		str+='Python'
	ans=Label(text="You learnt"+str,fg='blue')
	ans.place(x=50,y=150,width=200,height=20)
