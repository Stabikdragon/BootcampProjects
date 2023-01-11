from turtle import Turtle



STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.seth(90)
        self.shape("turtle")
        self.goto(STARTING_POSITION)
    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


# TODO: Create a turtle player that starts at the bottom of the screen and listen for the "Up"
#  keypress to move the turtle north. If you get stuck, check the video walkthrough in Step 3.
