from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

words_to_learn_path = r"day-31\flash-card-project-start\data\words_to_learn.csv"
csv_path = r"day-31\flash-card-project-start\data\french_words.csv"

# Get data from CSV
try:
    data = pandas.read_csv(words_to_learn_path)
except FileNotFoundError:
    data = pandas.read_csv(csv_path)

data_dict = data.to_dict(orient="records")
current_word = {}

def get_word():
    global timer, current_word
    window.after_cancel(timer)
    current_word = random.choice(data_dict)
    canvas.itemconfig(image_id, image=card_front)
    canvas.itemconfig(title_id, text="French", fill="black")
    canvas.itemconfig(text_id, text=current_word["French"], fill="black")
    timer = window.after(3000, flip_card)

def known_word():
    data_dict.remove(current_word)
    df = pandas.DataFrame(data_dict)
    df.to_csv(words_to_learn_path, index=False)
    get_word()

def flip_card():
    canvas.itemconfig(image_id, image = card_back)
    canvas.itemconfig(title_id , text= "English", fill="white" )
    canvas.itemconfig(text_id, text = current_word["English"], fill="white")


# Setup Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
timer = window.after(3000, flip_card)

# Canvas
canvas= Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file=r"day-31\flash-card-project-start\images\card_back.png")
card_front = PhotoImage(file=r"day-31\flash-card-project-start\images\card_front.png")
image_id = canvas.create_image(400,263, image = card_front)
title_id = canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic"))
text_id = canvas.create_text(400,263, text="Hello", font=("Ariel", 60, "bold"))
canvas.grid(row= 0,column= 0, columnspan=2)

# Right Button
check_image = PhotoImage(file=r"day-31\flash-card-project-start\images\right.png")
check_button = Button(image=check_image, highlightthickness=0, command=known_word)
check_button.grid(row=1 , column=1)

# Wrong Button
x_image = PhotoImage(file=r"day-31\flash-card-project-start\images\wrong.png")
wrong_button = Button(image=x_image, highlightthickness=0, command=get_word)
wrong_button.grid(row=1, column=0)

get_word()


window.mainloop()