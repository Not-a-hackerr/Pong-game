from turtle import Turtle
WIDTH = 5
LENGTH = 1


class Paddle(Turtle):
    def __init__(self, x_cood, y_cood):
        super().__init__()
        self.goto(x_cood, y_cood)
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=LENGTH, stretch_len=WIDTH)
        self.setheading(90)
        self.speed("fastest")

    def up(self):
        self.fd(20)

    def down(self):
        self.bk(20)
