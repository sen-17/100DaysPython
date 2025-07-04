# Functions with inputs

def greet(name):
    print(f"Hello {name}")
    print(f"Good Morning {name}")

greet("Jasson")

def my_function(something):
    print(something)

my_function(123)

# Positional vs Keyword Arguments
def greet_with(name , location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Jasson", "Indonesia")
