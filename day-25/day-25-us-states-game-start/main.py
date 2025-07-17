import turtle
import pandas

states_data = r"100DaysPython\day-25\day-25-us-states-game-start\50_states.csv"
image = r"100DaysPython\day-25\day-25-us-states-game-start\blank_states_img.gif"

screen = turtle.Screen()
screen.addshape(image)
screen.title("U.S States Guess")

tim = turtle.Turtle(shape=image)
text = turtle.Turtle()
text.hideturtle()
text.penup()

data = pandas.read_csv(states_data)
data_list = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50 :
    user_guess = turtle.textinput(title = f"{len(guessed_states)}/50 States Correct", prompt = "What's another state").title()

    if user_guess == "Exit":
        for guessed in guessed_states:
            if guessed in data_list:
                data_list.remove(guessed)
                
                data_dict = {
                    "missed states" : data_list,
                }
                convert_table = pandas.DataFrame(data_dict)
                convert_table.to_csv(r"100DaysPython\day-25\day-25-us-states-game-start\review.csv")
        break

    if user_guess in data_list and user_guess not in guessed_states:
        guessed_states.append(user_guess)
        guessed_row = data[data.state == user_guess]
        index = guessed_row.index[0]
        x = guessed_row.x[index]
        y = guessed_row.y[index]
        
       
        text.goto(x,y)
        text.write(f"{user_guess}", align="center")

screen.exitonclick()