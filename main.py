#imports
from turtle import Turtle, Screen
import time

#initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

#create snake segments
segments = []
start_positions = [(0,0), (-20,0), (-40,0)]
for position in start_positions:
    segment=Turtle(shape="square")
    segment.penup()
    segment.color("white")
    segment.goto(position)
    segments.append(segment)
    screen.update()

game_on = True
while game_on:
    for seg in segments:
        seg.forward(20)
        screen.update()
    time.sleep(0.2)

#exit conditions
screen.exitonclick()