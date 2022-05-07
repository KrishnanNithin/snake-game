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
            segment=Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
            for i in range(len(self.segments)-1, 0,-1):
                new_x = self.segments[i-1].xcor()
                new_y = self.segments[i-1].ycor()
                self.segments[i].goto(new_x, new_y)
            self.segments[0].forward(20)
