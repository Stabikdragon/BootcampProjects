import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
score = Scoreboard()

screen.title("Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

game_is_on = True

screen.listen()
player_1 = score.score
player_2 = 0
screen.onkey(r_paddle.up, "Up")
screen.onkeypress(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkeypress(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkeypress(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkeypress(l_paddle.down, "s")

while game_is_on:
    time.sleep(.08)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    if ball.xcor() > 320:
        player_1 += 1
        print(player_1)
    if ball.xcor() > -320:
        player_2 += 1
        print(player_2)


screen.exitonclick()


