from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITIONS = [-70, -40, -10, 20, 50, 80]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.ht()



    def create(self):
            new_turtle = Turtle()
            rand_position = random.randint(-240,240)
            rand_color = random.choice(COLORS)
            new_turtle.shape("square")
            new_turtle.penup()
            new_turtle.seth(180)
            new_turtle.turtlesize(1,2)
            new_turtle.setposition(240, rand_position)
            new_turtle.color(rand_color)
            self.cars.append(new_turtle)

    def move(self):
        for turtle in self.cars:
            turtle.forward(MOVE_INCREMENT)





# TODO: Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left
#  edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe
#  zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck,
#  check the video walkthrough in Step 4.
