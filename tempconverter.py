import tkinter
from tkinter import *
from tkinter import messagebox
from functools import partial

window = Tk()
window.title("Temperature Converter")
window.geometry("500x300")

tempval = "Celsius"

def temperature(set_tempr):
    global tempval
    tempval = set_tempr

def submit_action(labelres1, input11):
    temp = input11.get()

    if tempval == "Celsius":
        f = float((float(temp) * 9 / 5) + 32)
        labelres1.config(text="%.1f Fahrenheit" % f)
        messagebox.showinfo("Temperature Converter",
                            "Successfully converted to Fahrenheit ", )

    if tempval == "Fahrenheit":
        c = float((float(temp) - 32) * 5 / 9)
        labelres1.config(text="%.1f Celsius" % c)
        messagebox.showinfo("Temperature Converter",
                            "Successfully converted to Celsius ")
        return

window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(1, weight=1)

input1 = StringVar()
var= StringVar

label1 = Label(window, text="Enter Temperature")
label_entry = Entry(window, textvariable= input1)
label1.grid(row=1)
label_entry.grid(row=1, column=1)
labelresult = Label(window)
labelresult.grid(row=3, columnspan=4)

dropList = ["Fahrenheit", "Celsius"]
dropdown = OptionMenu(window, var, *dropList, command=temperature)
var.set = dropList[0]
dropdown.grid(row=1, column=2)

submit_action = partial(submit_action, labelresult, input1)
resbutton = Button(window, text="Convert", command=submit_action)
resbutton.grid(row=2, columnspan=2)

window.mainloop()