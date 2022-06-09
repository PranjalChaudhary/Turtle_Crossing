from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.level = 0

    def car_maker(self):
        i = random.randint(1, 6)
        if i == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto((300, random.randint(-250, 250)))
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.forward(STARTING_MOVE_DISTANCE + self.level * MOVE_INCREMENT)

    def level_up(self):
        """Changes the level to increase the speed of the cars"""
        self.level += 1

    def collision(self, player):
        """Checks for collision between the cars and the players"""
        for cars in self.all_cars:
            if cars.distance(player) < 20:
                return False
        return True
