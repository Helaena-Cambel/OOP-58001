from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry("500x250+10+20")
window.title("Midterm in OOP")

str1 = StringVar()
str2 = StringVar()

def name():
 prnt = (str1.get())
 str2.set(prnt)

label = Label(window, text = "Enter your fullname:", fg = "red")
label.place(x=60, y=70)

txtfld1 = Entry(window, bd = 3, textvariable=str1)
txtfld1.place(x=265, y=65)

button = Button(window, text = "Click to display your Fullname", fg = "red", command=lambda:name())
button.place (x=60, y=145)

txtfld2 = Entry(window, bd = 3, textvariable=str2)
txtfld2.place(x=265, y=145)

window.mainloop()