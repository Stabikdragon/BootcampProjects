from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.ht()
        self.speed = STARTING_MOVE_DISTANCE

    def create(self):
        new_turtle = Turtle()
        rand_position = random.randint(-240, 240)
        rand_color = random.choice(COLORS)
        new_turtle.shape("square")
        new_turtle.penup()
        new_turtle.shapesize(1, 2)
        new_turtle.setposition(240, rand_position)
        new_turtle.color(rand_color)
        self.cars.append(new_turtle)

    def move(self):
        for turtle in self.cars:
            new_x = turtle.xcor() - self.speed
            turtle.goto( new_x, turtle.ycor())

    def increase_speed(self):
        self.speed += MOVE_INCREMENT






