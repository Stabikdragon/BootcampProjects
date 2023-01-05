from turtle import Turtle, Screen

screen = Screen()
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0,280)
        self.score = 0
        self.write(f"test{self.score}", align="center", font=('Arial', 10, 'bold'))


