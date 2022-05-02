from turtle import Screen
import time
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
halil = Snake()
food = Food()
score = ScoreBoard()
screen.onkeyrelease(fun=halil.turn_right, key="Right")
screen.onkeyrelease(fun=halil.turn_left, key="Left")
screen.onkeyrelease(fun=halil.turn_up, key="Up")
screen.onkeyrelease(fun=halil.turn_down, key="Down")


is_on = True
while is_on:
    screen.update()

    time.sleep(0.1)
    if halil.segments[0].distance(food) < 15:
        food.refresh()
        halil.add_segment()
        score.score_up()

    halil.move()
    if halil.segments[0].xcor() > 300 or halil.segments[0].xcor() < -300 or halil.segments[0].ycor() < -300 or halil.segments[0].ycor() > 300:
        is_on = False
        score.game_over()

    for segment in halil.segments[2:]:
        if halil.segments[0].distance(segment) < 10:
            is_on = False
            score.game_over()


screen.exitonclick()
