#imports
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

#initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

#Initialize objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
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

    #detect food collisions
    if snake.segments[0].distance(food)<15:
        scoreboard.score += 1
        scoreboard.clear()
        scoreboard.rewrite()
        food.refresh()


#exit conditions
screen.exitonclick()