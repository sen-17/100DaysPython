
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


scissors =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

import random
computer_pick = random.randint(0,2)
player_move = ''
computer_move = ''

player_pick = int(input("What will you play? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if player_pick == 0:
    player_move = 'rock'
elif player_pick == 1:
    player_move = 'paper'
else:
    player_move = 'scissors'

if computer_pick == 0:
    computer_move = 'rock'
elif computer_pick == 1:
    computer_move = 'paper'
else:
    computer_move = 'scissors'

if player_move == "rock" and computer_move == "paper":
    print(f"You pick\n{rock}")
    print(f"Computer pick\n{paper}")
    print("You lose")

elif player_move == "scissors" and computer_move == "rock":
    print(f"You pick\n{scissors}")
    print(f"Computer pick\n{rock}")
    print("You lose")

elif player_move == "paper" and computer_move == "scissors":
    print(f"You pick\n{paper}")
    print(f"Computer pick\n{scissors}")
    print("You lose")

elif player_move == computer_move:
    
    if player_move == 'rock':
        print(f"You pick\n{rock}")
        print(f"Computer pick\n{rock}")
        print("You Tied!")
    elif player_move == 'paper':
        print(f"You pick\n{paper}")
        print(f"Computer pick\n{paper}")
        print(f"You Tied!")
    else:
        print(f"You pick\n{scissors}")
        print(f"Computer pick\n{scissors}")
        print(f"You Tied")

else:
    print(f"You pick\n{player_move}")
    print(f"Computer pick\n{computer_move}")
    print("You won!")



    
