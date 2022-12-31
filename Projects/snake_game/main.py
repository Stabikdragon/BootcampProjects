from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)



snake = Snake()


is_true = True
while is_true:
    screen.update()
    time.sleep(.1)
    snake.move()






# if turtle.position() > (270,0):
#     turtle.setheading(90)




























screen.exitonclick()