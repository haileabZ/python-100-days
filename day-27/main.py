# mile to km converter app in tkinter module
import tkinter

window = tkinter.Tk()
window.title("first gui")
window.minsize(width=400,height=250)

input = tkinter.Entry(width=15)
input.grid(column=2,row=1)

label1 = tkinter.Label(text="miles")
label1.grid(column=3,row=1)

label2 = tkinter.Label(text="is equal to")
label2.grid(column=1,row=2)

label3 = tkinter.Label(text="0")
label3.grid(column=2,row=2)

label4 = tkinter.Label(text="Km")
label4.grid(column=3,row=2)


def clicked():
    label3.config(text=round(float(input.get()) * 1.6,2))

btn1 = tkinter.Button(text="Calculate", command=clicked)
btn1.grid(column=2,row=3)






window.mainloop()





