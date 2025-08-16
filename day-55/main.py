from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def bold(*args, **kwargs):
        text = function(*args, **kwargs)
        return f'<b> {text} </b>'

    return bold

def make_italic(function):
    def italic(*args, **kwargs):
        text = function(*args, **kwargs)
        return f'<em> {text} </em>'
    
    return italic

def make_underlined(function):
    def underline(*args, **kwargs):
        text = function(*args, **kwargs)
        return f'<u> {text} </u>'
    
    return underline

@app.route('/')
def home():
    return '<h1 style="text-align:center">Guess a Number</h1>' \
    '<p> This is a paragraph. </p>' \
    '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTl5NHM0ZG85bHBvbWFkN2F3dDVrcjZ4eXZnMTl1dG9ybzYxYjFobiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/HwmDZaI4YEeZ2/100.webp" width=280/>' \

@app.route('/username/<name>')
@make_bold
@make_italic
def greet(name):
    return f'Hello {name}'

if __name__ == "__main__":
    app.run(debug=True)