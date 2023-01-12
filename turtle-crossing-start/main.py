import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
score = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
car = CarManager()

screen.onkeypress(player.move,"Up")
cars = car.cars



game_is_on = True
while game_is_on:
    car.create()
    player.game_repeat()
    for i in range(6):
        car.move()
        time.sleep(.06)
        screen.update()
        for x in cars:
            if x.distance(player) < 25 and x.xcor() == player.xcor():
                print("test")
                game_is_on = False







screen.exitonclick()









# TODO:Detect when the turtle player collides with a car and stop the game if this happens.
#  If you get stuck,
#  check the video walkthrough in Step 5.

#

# TODO:Create a scoreboard that keeps track of which level the user is on. Every time the
#  turtle player does a
#  successful crossing, the level should increase. When the turtle hits a car, GAME OVER
#  should be displayed in the
#  centre. If you get stuck, check the video walkthrough in Step 7.
