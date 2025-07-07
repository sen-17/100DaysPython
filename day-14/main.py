# Higher or Lower
from game_data import data
from art import header , vs
import random

def welcome():
    return header

def pick_data():
    random_data = random.sample(data , k= 2)
    
    a , b = random_data

    a_name , a_follower , a_description , a_country = a["name"], a["follower_count"], a["description"], a["country"]
    b_name , b_follower, b_description, b_country = b["name"], b["follower_count"], b["description"], b["country"]

    return a_name , a_follower, a_description, a_country, b_name , b_follower, b_description, b_country

def compare_data(a_name , a_follower, a_description, a_country, b_name , b_follower, b_description, b_country):
    print(f"Compare A: {a_name}, {a_description}, from {a_country} ")
    print(vs)
    print(f"Compare B: {b_name}, {b_description}, from {b_country} ")

    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    while guess not in ["a", 'b']:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    if a_follower > b_follower and guess == "a":
        return True
    elif b_follower > a_follower and guess == "b":
        return True
    else:
        return False
    
def main():
    print(welcome())
    score = 0
    while True:
        a_name , a_follower, a_description, a_country, b_name , b_follower, b_description, b_country = pick_data()
        guess = compare_data(a_name , a_follower, a_description, a_country, b_name , b_follower, b_description, b_country)

        if guess == True:
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            print(f"Sorry, You're Wrong! Score: {score}")
            break

if __name__ == "__main__":
    main()



    