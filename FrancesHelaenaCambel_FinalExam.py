from tkinter import *

window = Tk()
window.title("Find the least number among three numbers")
window.geometry("380x200+500+100")
window.configure(bg='powder blue')

def findLeast():
    L = []
    L.append(eval(conOfent2.get()))
    L.append(eval(conOfent3.get()))
    L.append(eval(conOfent4.get()))
    conOfLeast.set(min(L))

lbl1 = Label(window, bg='powder blue', text = "This program finds the least number")
lbl1.grid(row=0, column=1, columnspan=2, sticky=EW)
lbl2 = Label(window, bg='powder blue', text="Enter the first number:")
lbl2.grid(row=1, column=0, sticky=W)
conOfent2 = StringVar()
ent2 = Entry(window, bd=3, textvariable=conOfent2)
ent2.grid(row=1, column=1)
lbl3 = Label(window, bg='powder blue',  text="Enter the second number:")
lbl3.grid(row=2, column=0)
conOfent3 = StringVar()
ent3 = Entry(window, bd=3, textvariable=conOfent3)
ent3.grid(row=2, column=1)
lbl4 = Label(window, bg='powder blue', text="Enter the third number:")
lbl4.grid(row=3, column=0, sticky=W)
conOfent4 = StringVar()
ent4 = Entry(window,bd=3,textvariable=conOfent4)
ent4.grid(row=3, column=1)

btn1 = Button(window, bg='pink', text="Find the least number", command=findLeast)
btn1.grid(row=4, column=1)
lbl5 = Label(window, bg='powder blue', text="The least number:")
lbl5.grid(row=5, column=0, sticky=W)
conOfLeast = StringVar()
ent5 = Entry(window, bd=3, state="readonly", textvariable=conOfLeast)
ent5.grid(row=5, column=1)

mainloop()
