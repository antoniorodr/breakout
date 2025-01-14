from turtle import Screen
from paddle import Paddle, Ball, Scoreboard, Brick
from tkinter import messagebox
import time

BRICK_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
game_on = True
bricks = []

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 1300, height = 800)
screen.title("Breakout)")
screen.tracer(0)

paddle = Paddle((0, -320))
ball = Ball()
scoreboard = Scoreboard()

for n in range(len(BRICK_COLORS)):
    y_position = 300 - n * (30 + 10)
    color = BRICK_COLORS[n % len(BRICK_COLORS)]
    for x in range(-610, 650, 100):
        brick = Brick((x, y_position), color)
        bricks.append(brick)

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if scoreboard.lives == 0:
        messagebox.showinfo(message = f"Game Over. Final score: {scoreboard.score}. Thanks for playing!")
        screen.exitonclick()

    if ball.xcor() > 620 or ball.xcor() < - 620:
        ball.bounce_x()

    if ball.distance(paddle) < 35:
        ball.bounce_y()

    for brick in bricks:
        if ball.distance(brick) < 45:
            scoreboard.scoring()
            ball.bounce_y()
            bricks.remove(brick)
            brick.hideturtle()
            break 
    
    if ball.ycor() > 300:
        ball.bounce_y()

    if ball.ycor() < - 300:
        ball.reset_position()
        scoreboard.lose()
        time.sleep(1)

screen.exitonclick()