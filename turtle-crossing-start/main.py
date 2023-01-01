import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor("white")
player = Player()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
turtle.listen()
turtle.onkey(player.move,"w")
car_manager = CarManager()



game_is_on = True

while game_is_on:

    car_manager.move()
    car_manager.create_car()
    time.sleep(car_manager.move_speed)
    screen.update()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >=280:
        player.start()
        car_manager.speed_increase()
        scoreboard.increase_lvl()



screen.exitonclick()