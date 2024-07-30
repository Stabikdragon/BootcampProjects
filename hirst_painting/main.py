import turtle
from turtle import Turtle, Screen
import colorgram
import random

timmy = Turtle()
timmy.shape("turtle")
colors = colorgram.extract('image.jpg',30)
turtle.colormode(255)
timmy.speed("fastest")
list = []
is_true = True
timmy.penup()
heading = 180
timmy.setx(-200)

for i in colors:
    rgb =[]
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    rgb = (r,g,b)
    list.append(rgb)

for x in range(10):
    for y in range(1):
        timmy.==
        timmy.setx(-200)
        for i in range(10):
            random_color = random.choice(list)
            timmy.dot(20, random_color)
            timmy.forward(50)




screen = Screen()
screen.exitonclick()








