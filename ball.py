from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.penup()
        self.color("white")
        self.shape("circle")
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1.1
        
    def reposition(self):
        self.home()
        self.bounce_x()
        self.move()
        if self.x_move < 0:
            self.x_move = -10
        elif self.x_move > 0:
            self.x_move = 10





