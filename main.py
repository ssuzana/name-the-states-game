import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Name the States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")

count = 0
guess = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
guess_list = []

while count < 50:
    if guess in list(data.state) and guess not in guess_list:
        guess_list.append(guess)
        new_state = data[data["state"] == guess]
        output = turtle.Turtle()
        output.penup()
        output.hideturtle()
        output.goto(float(new_state.x), float(new_state.y))
        output.write(guess)
        count += 1
        guess = screen.textinput(title=f"{count}/50 Correct States", prompt="What's another state's name?").title()
    else:
        guess = screen.textinput(title=f"{count}/50 Correct States", prompt="What's another state's name?").title()

screen.exitonclick()
