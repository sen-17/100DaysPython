# Caesar Cipher

from art import logo

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text , shift_amount):
    shifted_text = []
    for char in original_text:
        if char in alphabets:
            check_index = alphabets.index(char)
            new_index = (check_index + shift_amount) % 26
            shifted_text.append(alphabets[new_index])
        else:
            shifted_text.append(char)
    
    return "".join(shifted_text)

def decrypt(shifted_text , shift_amount):
    original_text = []
    for char in shifted_text:
        if char in alphabets:
            check_index = alphabets.index(char)
            new_index = (check_index - shift_amount) % 26
            original_text.append(alphabets[new_index])
        else:
            shifted_text.append(char)
    
    return "".join(original_text)

def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypted = encrypt(text, shift)
        print(encrypted)
    elif direction == "decrypt":
        decrypted = decrypt(text , shift)
        print(decrypted)
    else:
        print("Please enter again.")

def try_again():
    ask = input("Do you want to try again? Y for yes and N for No: ").lower()
    return ask

while True:
    logo
    caesar()
    asked = try_again()
    if asked == "y":
        continue
    else:
        print("Thanks for using Caesar Cipher")
        break
    








    
        
