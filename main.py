import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.auto_drive()
    for x in carmanager.cars:
        if player.distance(x) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.finished_level():
        player.start_over()
        carmanager.increase_speed()
        scoreboard.add_level()


screen.exitonclick()


