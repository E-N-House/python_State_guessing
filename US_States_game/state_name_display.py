from turtle import Turtle

FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"


class StateName(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.state = state
        self.was_guessed = False

    def display_name(self):
        self.clear()
        self.write(arg=self.state, font=FONT, align=ALIGNMENT)

    def is_answer(self, answer):
        if self.state.lower() == answer:
            self.was_guessed = True
            return True
        else:
            pass
