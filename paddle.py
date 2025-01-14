from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position: tuple):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = 1.2, stretch_len =5)
        self.penup()
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

class Brick(Turtle):
    def __init__(self, position: tuple, color: str):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid = 1.5, stretch_len =4)
        self.penup()
        self.goto(position)
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.lives = 5
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 340)
        lives_text = f"Lives: {self.lives}"
        self.write(lives_text, align="center", font=("Courier", 30, "normal"))
        
        self.goto(300, 340)
        score_text = f"Your score: {self.score}"
        self.write(score_text, align="center", font=("Courier", 30, "normal"))

    def lose(self):
        self.lives -= 1
        self.update_scoreboard()

    def scoring(self):
        self.score += 1
        self.update_scoreboard()



if __name__ == "__main__":
    paddle = Paddle()