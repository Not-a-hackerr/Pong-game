from turtle import Turtle
FONT = ('Courier', 70, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def add_r_score(self):
        self.clear()
        self.r_score += 1

    def add_l_score(self):
        self.clear()
        self.l_score += 1

    def update(self):
        self.goto(-120, 200)
        self.write(f"{self.r_score}", font=FONT)
        self.goto(80, 200)
        self.write(f"{self.l_score}", font=FONT)


