from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.write(f"Score: {self.score}", align= "center", font=("Arial", 24, "normal"))

    def updateScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

