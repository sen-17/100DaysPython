# BackEnd Development Using Python
from flask import Flask
import time

app = Flask(__name__) # __main__ (special attribute)

@app.route("/") # Home Route, Python Decorators 
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run()


# 1. Passing in function
# def calculate(calc_function, n1 ,n2):
#     return calc_function(n1,n2)

# 2. Nested Function
# def outer_function():
#     print("I'm Outer")

#     def nested_function():
#         print("I'm Inner")

#     nested_function()

# outer_function()

# 3. Functions can be returned  from other functions
# def outer_function():
#     print("I'm Outer")

#     def nested_function():
#         print("I'm Inner")

#     return nested_function (without brackets)

# Python Decorator Function (give additional functionalities to functions)
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function

@delay_decorator
def say_hello():
    print('Hello')

@delay_decorator
def say_bye():
    print('Bye')
