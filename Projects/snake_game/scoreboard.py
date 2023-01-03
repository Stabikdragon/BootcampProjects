from turtle import Turtle

# score = Turtle()
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.number = 0
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0,200)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.number}", align="center", font=('Arial', 20, 'bold'))

    def increase_score(self):
        self.clear()
        self.number += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=('Arial', 20, 'bold'))





# TODO: turtle that knows how to keep track of the score and
#  how to display it in the program. font size and font type.
#  turtle.clear and turtle.write
