from tkinter import *

window = Tk()
window.title("First GUI Program")
window.minsize(width=500 , height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text= "Hello", font= ("Arial", 24, 'bold'))
my_label.grid(column=0, row=0)

# Multiple ways to change/update a properties
# my_label["text"] = "New Text"
# my_label.config(text= "New Text")

# Button
def button_clicked():
    text = input.get()
    my_label.config(text = text)

button = Button(text= "Click me", command= button_clicked)
button.grid(column = 1, row=1)

# Entry
input = Entry(width=10)
input.insert(END, string = "Some text to begin with" ) # add text to begin with
input.get() # get text in entry
input.grid(column=2 , row=1)

# Text
text = Text(height=5, width=30)
text.focus() # Puts cursor in textbox
text.insert(END, "Example of multi line text entry") # Add some text to begin with
text.get("1.0", END) # Gets current value in textbox at line 1 , character 0
text.grid(column=3 , row =1 )

#Spinbox
def spinbox_used():
    print(spinbox.get()) # gets current value in spinbox

spinbox = Spinbox(from_=0, to=10, width=5, command = spinbox_used)
spinbox.grid(column=4, row=1)

# Scale
def scale_used(value):
    print(value)

scale = Scale(from_ = 0, to = 100, command = scale_used)
scale.grid(column=5 , row=1)

# Check Button
def check_button_used():
    print(checked_state.get()) # Prints 1 if On button checked, otherwise 0

checked_state = IntVar() # variable to hold on to checked state, 0 is off , 1 is on
checkbutton = Checkbutton(text="Is On?", variable = checked_state, command = check_button_used)
checked_state.get()
checkbutton.grid(column=6 ,row=1)

# Radio Button
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radio_button1 = Radiobutton(text = "Option 1", value=1 , variable = radio_state, command=radio_used)
radio_button2 = Radiobutton(text = "Option 2", value=2 , variable = radio_state, command=radio_used)
radio_button1.grid(column=7 , row = 1)
radio_button2.grid(column=7 , row= 2)

# List Box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["banana", "apple", "pear"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=8, row=1)

# Layout 
#.pack(side=" ")
# Place(x,y)
# Grid(column , row)

# Advance Python Arguments
# Arguments with Default Values
def add(*args): # tuple type
    total = sum(args)
    print(total)

add(1,2,3)


# kwargs : many keyword arguments
def calculate(n , **kwargs): # dictionary
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n) #25

calculate(2 , add=3 , multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make = "Nissan")
print(my_car.model)


window.mainloop()