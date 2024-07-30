
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width = 500,height = 500)

user_bet = screen.textinput(title="Make your bet", prompt = "Which turtle will win?")

colors = ["red", "orange", "yellow", "green","blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

for i in range(0,6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("fastest")
    new_turtle.penup()
    new_turtle.setposition(-240, y_positions[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.position() > (230, 0):
            print(f"the winner is : {turtle.color()[0]}")
            is_race_on = False
screen.exitonclick()