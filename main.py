from turtle import Screen, Turtle
from paddle import Paddle, Ball, Scoreboard, Brick
from tkinter import messagebox
import time

BRICK_COLORS = ["IndianRed1", "LightSalmon1", "LightGoldenrod1", "LightGreen", "DodgerBlue1", "LightPink1"]
game_on = True
bricks = []

CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')

screen = Screen()
screen.bgcolor("gray20")
screen.setup(width = 1300, height = 800)
screen.title("Breakout")
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

    if scoreboard.score == 468:
        messagebox.showinfo(message = f"You won!. Final score: {scoreboard.score}. Thanks for playing!")
        screen.exitonclick()

    if ball.xcor() > 620 or ball.xcor() < - 620:
        ball.bounce_x()

    if (ball.ycor() > -320 and ball.ycor() < -320 + 24) and \
       (ball.xcor() > paddle.xcor() - 100/ 2 and ball.xcor() < paddle.xcor() + 100 / 2):
        ball.bounce_y()

    for index, brick in enumerate(bricks):
        if ball.distance(brick) < 40:
            row_index = index // 13
            score_increment = 2 * (5 - row_index) + 1
            scoreboard.scoring(score_increment)
            ball.bounce_y()
            bricks.remove(brick)
            brick.hideturtle()
            break
    
    if ball.ycor() > 300:
        ball.bounce_y()

    if ball.ycor() <= - 350:
        ball.reset_position()
        scoreboard.lose()
        paddle.start_position((0, -320))
        time.sleep(1)

screen.exitonclick()