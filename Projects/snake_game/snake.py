
from turtle import Screen, Turtle

screen = Screen()
LOCATION = [(-20,0), (0,0), (20,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.n_turtles = []
        self.create_turtle()
        self.head = self.n_turtles[0]
        self.click()

    def create_turtle(self):
        for position in LOCATION:
            tim = Turtle("square")
            tim.penup()
            tim.speed("fast")
            tim.color("white")
            tim.setposition(position)
            self.n_turtles.append(tim)

    def move(self):

            for turtle in range(len(self.n_turtles) - 1, 0, -1):
                new_x = self.n_turtles[turtle - 1].xcor()
                new_y = self.n_turtles[turtle - 1].ycor()
                self.n_turtles[turtle].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)
    def click(self):
        def up():
            if self.head.heading() != DOWN:
                self.head.setheading(UP)

        def down():
            if self.head.heading() != UP:
                self.head.setheading(DOWN)

        def left():
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)

        def right():
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)

        screen.listen()
        screen.onkey(up, "Up")
        screen.onkey(down, "Down")
        screen.onkey(left, "Left")
        screen.onkey(right, "Right")