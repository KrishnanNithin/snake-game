#imports
from turtle import Turtle, Screen

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(-30, 250)
        self.color("white")
        self.rewrite()
    
    def rewrite(self):
        self.clear()
        self.write(f'Score = {self.score}', align="center",font=('Arial', 15, 'normal'))

