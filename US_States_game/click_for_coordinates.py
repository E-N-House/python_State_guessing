import turtle

screen = turtle.Screen()
# screen.setup(width=800, height=600)
screen.title("U.S.A. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# screen.bgpic("blank_states_img.gif")
# screen.bgcolor("light blue")


# find coordinates of a point
def print_coordinates(x, y):
    """Print x and y coordinates"""
    print(x, y)


# notice mouse clicks
turtle.onscreenclick(print_coordinates)


# keep main loop going
turtle.mainloop()
