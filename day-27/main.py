from tkinter import *
# window = Tk()
# window.title("My first GUI program")
# window.minsize(600,600)
# window.config(padx=20, pady = 20)
#
#
# my_label = Label(text = "I am a label", font = ("Arial", 10, "bold"))
# my_label.grid(column= 0, row = 0)
#
# input = Entry()
# input.grid(column= 1, row = 1)
#
# def button_click():
#     print("i got clicked")
#     my_label["text"] = input.get()
#
#
#
# button = Button(text= "click here", command = button_click)
# button.grid(column= 3, row = 0)
#
# new_button = Button(text = "new button")
# new_button.grid(column=4, row = 3)
# new_button.config(padx=20, pady = 20)
#

window = Tk()
window.title("Mile to Km Converter")
window.minsize(100,5 0)
window.config(padx= 20, pady= 20)


input = Entry(width=10)
input.grid(row = 0, column = 1)
input.insert(END, string= '0')

label_1 = Label(text = "Miles")
label_1.grid(row = 0, column = 2)

label_2 = Label(text = "is equal to")
label_2.grid(row = 1, column = 0)

label_3 = Label(text = 0)
label_3.grid(row= 1, column =1)


label_4 = Label(text = "Km")
label_4.grid(row=1, column = 2)

def calculate():
    km = float(input.get()) * 1.609344
    label_3["text"] = round(km,2 )


button = Button(text = "Calculate", command = calculate)
button.grid(row=2, column = 1)




window.mainloop()
