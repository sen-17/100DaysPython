#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os

name_path = r"100DaysPython\day-24\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt"
letter_path = r"100DaysPython/day-24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt"
output_dir = r"100DaysPython\day-24\Mail+Merge+Project+Start\Mail Merge Project Start\Output"

with open(name_path , mode='r') as file:
    names = [name.strip() for name in file.readlines()]

with open(letter_path , mode='r') as file:
    letter_template = file.read()

for name in names:
    personalized_letter = letter_template.replace("[name]", name)
    output_path = os.path.join(output_dir, f"letter_for_{name}.txt")

    with open(output_path, mode="w") as out_file:
        out_file.write(personalized_letter)
    
        
        




