from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.setheading(90)
        self.goto(position)
        self.speed("fastest")

    def up(self):
        self.forward(30)

    def down(self):
        self.backward(30)


