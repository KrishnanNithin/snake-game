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

#initialize and define listeners
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.right, "d")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.07)
    snake.move()


#exit conditions
screen.exitonclick()