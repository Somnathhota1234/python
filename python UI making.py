from tkinter import *
parent= Tk()
parent.geometry("280x150")
label1=Label(parent, text="first name ", fg="blue").place(x=20, y=20)
label2=Label(parent, text="last name ", fg="blue").place(x=20, y=45)

entry1=Entry().place(x=95, y=20)
entry2=Entry().place(x=95, y=45)

button1=Button(text="submit").place(x=100, y=90)
parent.mainloop()
