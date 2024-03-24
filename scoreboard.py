from turtle import Turtle

with open("data.txt", mode="r") as file:
    highscore = int(file.read())

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.highscore = highscore
        self.score = 0
        self.goto(x=0, y=255)

    def write_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score = {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.write_score()
