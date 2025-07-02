# Password Generator
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
           ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welcome to the PyPassword Generator!")
length = int(input("How many letters do you want?"))
digit = int(input("How many numbers do you want?"))
symbol = int(input("How many symbols do you want? "))

random_let = random.choices(letters , k= length)
random_num = random.choices(numbers, k=digit)
random_symbol = random.choices(symbols, k=symbol)

combine = random_let + random_num + random_symbol

random.shuffle(combine)

password = ''.join(combine)
print(password)







