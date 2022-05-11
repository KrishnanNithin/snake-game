#imports
import time
from turtle import Turtle

start_positions = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in start_positions:
            self.add_segment(position)

    def add_segment(self, position):
        segment=Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
            for i in range(len(self.segments)-1, 0,-1):
                new_x = self.segments[i-1].xcor()
                new_y = self.segments[i-1].ycor()
                self.segments[i].goto(new_x, new_y)
            self.segments[0].forward(20)
    
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

