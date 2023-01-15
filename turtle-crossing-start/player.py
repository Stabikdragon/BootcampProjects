from turtle import Turtle
import time



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

    def game_repeat(self):
            time.sleep(1)
            self.clear()
            self.goto(STARTING_POSITION)



