print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************    
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

choose = input("Which direction do you want to go? Right or Left: ").lower()

if choose == "right":
    print("You Fall into a Hole.\nGame Over.")
elif choose == "left":
    action = input("You encounter a lake. Do you want to swim or wait? ").lower()
    if action == "swim":
        print("You got Attacked by trout.\nGame Over")
    elif action == "wait":
        door = input("You discovered a door. Which door do you want to open? (Red, Blue , Yellow): ").lower()
        if door == "red":
            print("You got burned by fire.\nGame Over")
        elif door == "yellow":
            print("Congratulations! You won!")
        elif door == "blue":
            print("You got eaten by beasts.\n Game Over.")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over")

