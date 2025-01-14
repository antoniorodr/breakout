from turtle import Screen
from paddle import Paddle, Ball, Scoreboard, Brick
import time

brick_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 1300, height = 800)
screen.title("Breakout)")
screen.tracer(0)

paddle = Paddle((0, -320))
ball = Ball()
scoreboard = Scoreboard()

for n in range(len(brick_colors)):
    y_position = 300 - n * (30 + 10)
    color = brick_colors[n % len(brick_colors)]
    for x in range(-610, 650, 100):
        Brick((x, y_position), color)


screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 620 or ball.xcor() < - 620:
        ball.bounce_x()

    if ball.distance(paddle) < 30:
        ball.bounce_y()
    
    if ball.ycor() > 300:
        ball.bounce_y()

    if ball.ycor() < - 300:
        ball.reset_position()
        scoreboard.lose()

screen.exitonclick()