#imports
from turtle import Turtle, Screen

from sqlalchemy import Integer

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.goto(-30, 250)
        self.color("white")
        self.rewrite()
    
    def rewrite(self):
        self.clear()
        self.write(f'Score = {self.score} High score = {self.high_score}', align="center",font=('Arial', 15, 'normal'))

    def end_game(self):
        if self.score > self.high_score:
            self.clear()
            self.high_score = self.score
            self.write(f'Game Over! Final score = {self.score} High score = {self.high_score}', align="center",font=('Arial', 15, 'normal'))
            self.score = 0
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.high_score))
        else:
            self.clear()
            self.write(f'Game Over! Final score = {self.score} High score = {self.high_score}', align="center",font=('Arial', 15, 'normal'))
            self.score = 0