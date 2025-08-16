from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=280 />'

random_num = random.randint(0,9)

@app.route('/<int:num>')
def check(num):
    user_input = num

    if user_input < random_num:
        return '<h1 style="color:red">Too low, Try Again!</h1>' \
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"  />'
    elif user_input > random_num:
        return'<h1 style="color:purple">Too High, Try Again!</h1>' \
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"  />'
    else:
        return'<h1 style="color:green">You Found me!</h1>' \
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'

if __name__ == "__main__":
    app.run()