import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

players = Player()
screen.listen()
screen.onkey(players.move_up, key="Up")
cars = CarManager()
score = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    cars.car_maker()
    cars.move_cars()

    # Checks collision of player and cars
    game_is_on = cars.collision(players)
    if not game_is_on:
        score.game_over()

    # Check whether player has won the level
    if players.ycor() >= 280:
        players.reset_player()
        cars.level_up()
        score.update_level()
    screen.update()

screen.exitonclick()
