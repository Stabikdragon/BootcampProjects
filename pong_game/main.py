from paddle import Paddle
from turtle import Screen,Turtle
from scoreboard import Scoreboard
from ball import Ball
import random




screen = Screen()
score = Scoreboard()


screen.title("Pong")
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()




game_is_on = True

screen.listen()

screen.onkey(r_paddle.up,"Up")
screen.onkeypress(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkeypress(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkeypress(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")
screen.onkeypress(l_paddle.down,"s")

ball.setheading(random.randint(0, 270))

while game_is_on:
    screen.update()
    # ball.forward(.1)

    # if ball.distance(r_paddle.position()) < 2  or ball.distance(l_paddle.position()) < 2:
    #     ball.setheading(random.randint(0, 270))
    # elif ball.xcor() > 760 or ball.xcor() < -760 or ball.ycor() > 560 or ball.ycor() < -560:
    #     ball.setheading(random.randint(0, 270))



screen.exitonclick()


# paddle - width 20, height 100. x_pos = 350, y_post 0.


