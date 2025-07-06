import random

def welcome():
    print('Welcome to Number Guessing Game!')
    print("I'm thinking of a random number..")

def random_number():
    return random.randint(1,100)

def difficulty_easy():
    return 10

def difficulty_normal():
    return 5

def difficulty_hard():
    return 3

def choose_difficulty():
    ask = input("What difficulty do you want to play? Easy , Normal , or Hard:  ").lower()

    if ask == "easy":
        return difficulty_easy()
    elif ask == "normal":
        return difficulty_normal()
    elif ask == "hard":
        return difficulty_hard()
    else:
        print("Invalid input. Defaulting to Normal.")
        return difficulty_normal()

def logic(guess , target, chance):
    if guess == target:
        message =  f"You won! the number was {target}"
        return chance , message
    else:
        chance -= 1
        if guess > target:
            message = f"{guess} is higher than the number."
        else:
            message = f"{guess} is lower than the number."
        return chance, message

def main():
    welcome()
    target_num = random_number()
    chance = choose_difficulty()
    print(f"Your chance: {chance}")
   
    while chance > 0:
        try:
            guess = int(input("Guess a number: "))
        except ValueError:
            print("Please enter a valid number!")

        chance , message = logic(guess, target_num, chance)
        print(message)

        if guess == target_num:
            break
    
        if chance == 0:
            print(f"You've run out of chances. The number was {target_num}")
        else:
            print(f"Chances left: {chance}")
      

if __name__ == "__main__":
    main()




