from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.penup()
        self.goto(0, 270)
        self.write(f"Level {self.level}", font=FONT, align='Center')

    def update_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto((0, 0))
        self.write("GAME OVER !!", align="Center",font=FONT)
