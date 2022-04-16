from tkinter import *
from tkinter import ttk
window = Tk()

window.geometry("400x230+10+20")
window.title("Main GUI")

button = Button (window, text = "Button", fg = "red", font = ("Verdana", 16))
button.place(x=190, y=20)

label = Label(window, text = "This is a label", fg = "blue", bg = "orange")
label.place(x=90, y=150)

txtfld = Entry(window, text = "This is a text field", bd = 5)
txtfld.place(x=180, y=148)

v1 = IntVar()
radiobutton = Radiobutton(window, text = "Male", variable = v1, value = 1)
radiobutton1 = Radiobutton(window, text = "Female", variable = v1, value = 2)
radiobutton.place(x=90, y=45)
radiobutton1.place (x=90, y=25)

v2 = StringVar()
v2.set("Student1")
data1 = "Student1", "Student2", "Student3"
combo = ttk.Combobox(window, values = data1)
combo.place(x=200, y=95)

data = "Student1", "Student2", "Student3"
lb = Listbox(window, height = 3, selectmode = "multiple")
for num in data:
    lb.insert(END, num)
lb.place(x=60, y=80)

window.mainloop()