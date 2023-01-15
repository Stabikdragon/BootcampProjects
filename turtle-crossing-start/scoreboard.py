from turtle import Turtle

FONT = ("Courier", 30 , "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.level = 1
        self.write_level()


    def write_level(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def add_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font=FONT)
