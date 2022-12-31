from turtle import Turtle, Screen
import random


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("DarkRed", "black")
timmy_the_turtle.speed("normal")



for i in range(100):
    current_heading = timmy_the_turtle.heading()

    timmy_the_turtle.circle(100)
    timmy_the_turtle.setheading(current_heading + 10)







screen = Screen()
screen.exitonclick()
