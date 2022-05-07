#imports
from turtle import Turtle, Screen
from snake import Snake
import time

#initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

#create snake object
snake = Snake()
screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


#exit conditions
screen.exitonclick()