import time
from scoreboard import Scoreboard
from turtle import Screen
from player import Player
from car_manager import CarManager






screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score = Scoreboard()
car = CarManager()
player = Player()
screen.listen()


screen.onkeypress(player.move,"Up")
cars = car.cars



game_is_on = True

while game_is_on:
    car.create()
    score.write_level()
    for i in range(6):
        car.move()
        time.sleep(.06)
        screen.update()
        for x in cars:
            if x.distance(player) < 20:
                score.game_over()
                game_is_on = False
            if player.ycor() > 280:
                player.game_repeat()
                score.add_level()
                car.increase_speed()








screen.exitonclick()










