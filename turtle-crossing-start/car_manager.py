from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITIONS = [-70, -40, -10, 20, 50, 80]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create()
        self.move()


    def create(self):
        for i in range(0, 6):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.seth(180)
            new_turtle.setposition(240, POSITIONS[i])
            new_turtle.color(COLORS[i])
            self.cars.append(new_turtle)
            self.move()
    def move(self):
        new_x= self.xcor() - MOVE_INCREMENT
        self.goto(self.ycor(), new_x)




# TODO: Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left
#  edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe
#  zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck,
#  check the video walkthrough in Step 4.
