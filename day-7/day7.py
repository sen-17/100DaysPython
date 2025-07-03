import random

word_list = ["aardvark", "baboon", "camel"]
lives = 6
guessed_letters = []
secret_word = random.choice(word_list)
current_display = ["_"] * len(secret_word)

def reveal_letters(secret_word , current_display, guess):
    result = []
    for secret_char , display_char in zip(secret_word, current_display):
        if secret_char == guess:
            result.append(guess)
        else:
            result.append(display_char)
    return(result)

while "_" in current_display and lives > 0:
    print("\nWord:", " ".join(current_display))
    print("Lives left:", lives)
    print("Guessed letters:", " ".join(guessed_letters))

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        current_display = reveal_letters(secret_word, current_display, guess)
        print("Correct!")
    else:
        lives -= 1
        print("Wrong!")

if "_" not in current_display:
    print("\n🎉 You won! The word was:", secret_word)
else:
    print("\n💀 Game over! The word was:", secret_word)









