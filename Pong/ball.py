from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0,0).
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9


    def paddle_bounce(self):
        self.x_move *= -1


    def restart(self):
        self.move_speed = 0.1
        self.home()
        self.paddle_bounce()
