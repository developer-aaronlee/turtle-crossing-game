from turtle import Turtle
FONT = ("Courier", 24, "normal")
POSITION = (-270, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.update_board()

    def update_board(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def add_level(self):
        self.clear()
        self.level += 1
        self.update_board()

    def game_over(self):
        self.goto(-50, 0)
        self.write("Game Over", align="left", font=FONT)
