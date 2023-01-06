from turtle import Turtle
import time
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("c ircle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed= 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.5

    def reset(self):
        time.sleep(2)
        self.bounce_x()
        self.home()
        self.move_speed = 0.1

