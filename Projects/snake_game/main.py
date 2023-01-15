from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

scoreboard = Scoreboard()



is_true = True
while is_true:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        is_true = False
        print(snake.head.distance(segment))
    for segment in snake.n_turtles[1:]:
        #

        # if snake.head.distance(segment) < 20:
        #     print(snake.head.distance(segment))
        #     is_true = False
        #     scoreboard.game_over()
screen.exitonclick()
