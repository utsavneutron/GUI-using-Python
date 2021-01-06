from tkinter import *

window = Tk()


def converttomiles():
    print(e1_value.get())
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)


b1 = Button(window, text='Execute', command=converttomiles)
b1.grid(row=0, column=1, rowspan=3)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=0)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)
window.mainloop()
