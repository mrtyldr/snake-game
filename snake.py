from turtle import Turtle, Screen


class Snake:

    def __init__(self):

        self.segments = []
        new_xcor = 0
        for i in range(0, 3):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(new_xcor, 0)
            new_xcor -= 20
            self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_xcor = self.segments[i-1].xcor()
            new_ycor = self.segments[i-1].ycor()
            self.segments[i].goto(new_xcor, new_ycor)
        self.segments[0].forward(20)

    def turn_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def turn_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def turn_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def turn_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)
