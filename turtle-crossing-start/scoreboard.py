from turtle import Turtle

FONT = ("Courier", 50 , "normal")


class Scoreboard(Turtle):
    def __int__(self):
        super().__init__()
        self.goto(0,0)
        self.color("black")
        self.penup()
        self.write("test", align="center", font=('Arial', 50, 'bold'))
