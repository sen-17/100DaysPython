import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv(r"day-26\NATO-alphabet-start\nato_phonetic_alphabet.csv")

letter_dict = {row.letter : row.code for (index , row ) in data.iterrows()}

user_name = input("What's your name? ").upper()
x = [let for let in user_name]

result = [letter_dict[letter] for letter in x if letter in letter_dict]
print (result)

# for (key,value) in letter_dict.items():
#     print(key)
#     print(value)




#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

