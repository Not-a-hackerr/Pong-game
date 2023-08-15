from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time




screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
#tracer turns off the animation therefore you need to update the screen


left_p = Paddle(-350, 0)
right_p = Paddle(350, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(fun=right_p.up, key="Up")
screen.onkey(fun=right_p.down, key="Down")
screen.onkey(fun=left_p.up, key="w")
screen.onkey(fun=left_p.down, key="s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    score.update()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if ball.distance(right_p) < 60 and ball.xcor() > 320 or \
            ball.distance(left_p) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reposition()
        score.add_r_score()

    elif ball.xcor() < - 380:
        ball.reposition()
        score.add_l_score()

screen.exitonclick()
