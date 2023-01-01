from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.level = 1
        self.score = Turtle()
        self.score.color("black")
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(-280, 250)
        self.score.write(f"Level: {self.level}", align="left", font=("Courier", 24, "bold"))
    def increase_lvl(self):
        self.score.clear()
        self.level+=1
        self.score.write(f"Level: {self.level}", align="left", font=("Courier", 24, "bold"))
    def game_over(self):
        self.score.goto(-70, 0)
        self.score.write(f"Game over", align="left", font=("Courier", 24, "bold"))