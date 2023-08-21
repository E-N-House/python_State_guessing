import turtle
from state_name_display import StateName

# TODO: make turtle background that is a state
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S.A. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# Alt to make bacground a photo rather then a shape and turtle
# screen.bgpic("blank_states_img.gif")
screen.bgcolor("light blue")

test_name = StateName("Kansas", 0, 0)
test_name.display_name()

# TODO: make a prompt that takes a state name and has a submit button
user_answer = screen.textinput(title= "Your Guess",prompt="Type a state name.").lower()
#     on submit will check if value exists in list
#       if yes
#             will place values on screen and display if there
#             Can do this by 50 indivudul turtle elements with on or off switch
#             score updates with each correct answer score/50
#       if no
#             prompt reappears
# TODO: list of states and if guessed or not
# TODO: score out of 50
#     score updates with each correct answer score/50

screen.exitonclick()