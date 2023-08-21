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
correct_guesses = []
# corrects = 0
attempts = 0

game_is_on = True
while game_is_on:
    # prompt that takes a state name and has a submit button
    user_answer = screen.textinput(title= f"{len(correct_guesses)}/50 states correct",prompt="Type a state name.").title()
    # does user want to leave game and get study list?
    if user_answer == "Exit":
        states_to_learn_data.state.to_csv("states_to_learn.csv")
        print(states_to_learn_data.state)
        game_is_on = False
        pass
    # on submit will check if value exists in list
    curr_guess = data[data.state == user_answer]
    # remove the entry if it has already been guessed
    states_to_learn_data = data.drop(data[data.state.str.lower() == user_answer].index)
    # check if the answer is already accounted for in string of answers
    if user_answer in correct_guesses:
        pass
    # will place values on screen and display if there
    elif len(curr_guess) == 1:
        # transform values from dataframe into strings or ints as needed
        curr_state = curr_guess.state.item()
        curr_x = int(curr_guess.x.item())
        curr_y = int(curr_guess.y.item())
        # record list of guesses
        correct_guesses.append(curr_state)
        # create the new stateName
        StateName(curr_state, curr_x, curr_y)
        # score updates with each correct answer score/50
        # corrects += 1
        # check if win condition met
        if len(correct_guesses) == 50:
            win_message = StateName("You win!! \n All 50 Guessed", 0, 0)
            Font = ("Courier", 50, "normal")
            win_message.display_name(font=Font)
            game_is_on = False
    else:
        # prompt reappears
        pass

screen.exitonclick()