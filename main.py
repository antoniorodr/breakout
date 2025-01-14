from turtle import Screen
from paddle import Paddle, Ball, Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 1300, height = 800)
screen.title("Breakout)")
screen.tracer(0)

paddle = Paddle((0, -320))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.xcor() > 320 or ball.distance(paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        

    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()