from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200 , height=200)
window.config(padx=20, pady=20)

label_1 = Label(text="Miles")
label_1.grid(column=3 , row=1)

input_1 = Entry(width=10)
input_1.grid(column=2 , row=1)

label_2 = Label(text="is equal to")
label_2.grid(column=1 , row=4)

input_2 = Entry(width=10)
input_2.grid(column=2 , row = 4)

label_3 = Label(text="Km")
label_3.grid(column=3, row = 4)

def calculate():
    miles = float(input_1.get())
    convert_to_km = miles * 1.6
    input_2.insert(END , string=f"{convert_to_km:.0f}")

button = Button(text="Calculate", command= calculate)
button.grid(column = 2 , row=6)







window.mainloop()