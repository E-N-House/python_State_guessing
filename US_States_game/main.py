import turtle
from state_name_display import StateName
from state_data import data

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S.A. States Game")
# Display map as image on screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.bgcolor("light blue")

# Alt to make background a photo rather then a shape and turtle
# screen.bgpic("blank_states_img.gif")

# store guesses
correct_guesses = ""
corrects = 0

game_is_on = True
while game_is_on:
    # prompt that takes a state name and has a submit button
    user_answer = screen.textinput(title= f"{corrects}/50 states correct",prompt="Type a state name.").lower()
    # on submit will check if value exists in list
    curr_guess = data[data.state.str.lower() == user_answer]
    # remove the entry if it has already been guessed
    # data = data.drop(data[data.state.str.lower() == user_answer].index)
    # check if the answer is already accounted for in string of answers
    if correct_guesses.find(user_answer) != -1:
        pass
    # will place values on screen and display if there
    elif len(curr_guess) == 1:
        # transform values from dataframe into strings or ints as needed
        curr_state = curr_guess.state.item()
        curr_x = int(curr_guess.x.item())
        curr_y = int(curr_guess.y.item())
        # record list of guesses
        correct_guesses += f" {curr_state.lower()}"
        # create the new stateName
        StateName(curr_state, curr_x, curr_y)
        # score updates with each correct answer score/50
        corrects += 1
    else:
        # prompt reappears
        pass

screen.exitonclick()