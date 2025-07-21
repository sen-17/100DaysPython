from tkinter import * 
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
           ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

def generate():
    password_entry.delete(0 , END)
    length = random.randint(8,10)
    digit = random.randint(1,10)
    symbol = random.randint(1,10)

    random_let = random.choices(letters , k= length)
    random_num = random.choices(numbers, k=digit)
    random_symbol = random.choices(symbols, k=symbol)

    combine = random_let + random_num + random_symbol
    random.shuffle(combine)

    password = ''.join(combine)
    pyperclip.copy(password)
    password_entry.insert(END , string = password)

def search_password():
    website = website_entry.get().title()
    try:
        with open(file_path, "r") as data_file:
            data = json.load(data_file)

            email = data[website]["email"]
            password = data[website]["password"]
            print(email, password)

            messagebox.showinfo(title = f"{website} credentials", message = f"email:{email}\npassword:{password}")
    except (ValueError, FileNotFoundError, KeyError):
        messagebox.showinfo(title="Error", message="No Data File Found")

# ---------------------------- SAVE PASSWORD ------------------------------- #
file_path = r"day-29\password-manager-start\data.json"
def save():
    website_name = website_entry.get().title()
    used_password = password_entry.get()
    used_email = email_entry.get()

    new_data = {
        website_name : {
            "email": used_email,
            "password": used_password
        }
    }

    if len(website_name) == 0 or len(used_password) == 0 or len(used_email) == 0:
        messagebox.showinfo(title= "Warning", message="Please input details")

    else:
        try:
            with open(file_path , mode="r") as file:
                data = json.load(file)
                data.update(new_data)
            
            with open(file_path, "w") as file:    
                json.dump(data, file, indent=4)
                
                website_entry.delete(0, END)
                password_entry.delete(0, END)

        except FileNotFoundError:
            with open(file_path, "w") as file:
                json.dump(new_data , file, indent = 4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=300, height=200)
lock_image = PhotoImage(file = r"day-29\password-manager-start\logo.png")
canvas.create_image(100,100 ,image = lock_image)
canvas.grid(row=2 , column = 2, sticky="w")

# Website
website_text = Label(text="Website:", font=("Arial", 12, "normal"))
website_text.grid(row=3 , column=1)

website_entry = Entry(width=43)
website_entry.grid(row=3 , column=2, sticky="w")
website_entry.focus()

search_website = Button(text="Search", width=15, command=search_password)
search_website.grid(row=3 ,column =2 , sticky="e" )

# Email
email_text = Label(text="Email/Username:", font=("Arial", 12, "normal"))
email_text.grid(row=4 , column=1)

email_entry = Entry(width=43)
email_entry.grid(row=4 , column=2, sticky="ew")
email_entry.insert(0, "johndoe@gmail.com")

# Password
password_text = Label(text="Password:", font=("Arial", 12, "normal"))
password_text.grid(row=5 , column=1)

password_entry = Entry(width=30, justify="left")
password_entry.grid(row=5, column=2, sticky="w")

generate_button = Button(text="Generate Password", width=15, command=generate)
generate_button.grid(row=5, column=2, sticky="e")

# Add 
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=6, column=2, sticky="ew")

window.mainloop()