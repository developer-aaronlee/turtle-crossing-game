from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def add_cars(self):
        for x in range(random.randint(10, 40)):
            self.create_car()

    def create_car(self):
        ran_chance = random.randint(1, 6)
        if ran_chance == 1:
            ran_ycor = random.randint(-250, 250)
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, ran_ycor)
            self.cars.append(new_car)

    def auto_drive(self):
        for x in self.cars:
            x.setheading(180)
            x.forward(self.speed)
            if x.xcor() < -300:
                x.goto(250, random.randint(-250, 250))

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

