# Functions with Outputs

def my_function():
    result = 3 * 2
    return result

print(my_function())

def format_name(f_name , l_name):
    # Docstrings 
    """
    Take first name and last name then combining them into a title cased name.
    """
    combine = f_name + " " + l_name

    return combine.title()

print(format_name("JASSON","TAN"))

def add(n1 , n2):
    return n1+n2

my_favorite_operation = add

print(my_favorite_operation(2,3))



