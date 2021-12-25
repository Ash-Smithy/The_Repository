from tkinter import *
def do_something():
    n = int(e1.get())
    product = 1 
    for i in range(1,n+1):
        product *= i
    value.set(product)
root = Tk()
topf = Frame()
midf = Frame()
bottf = Frame()
Label1 = Label(topf,text = "enter number to find the factorial for : ")
e1 = Entry(topf,width = 10)
e1.pack(side = 'right')
Label1.pack(side = 'left')
answer = Label(midf, text = 'factorial is : ')
value = StringVar()
fact_value = Label(midf,textvariable=value)
answer.pack()
fact_value.pack()
mybutton = Button(bottf,text = 'find the factorial',command = do_something)
mybutton.pack()
topf.pack(side = 'top')
midf.pack()
bottf.pack(side = 'bottom')
root.mainloop()