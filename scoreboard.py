from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.write_score()

    def score_up(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(arg=f"Score:{self.score}", move=False, align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game over", move=False, align="center")

