import random
import turtle as t

screen = t.Screen()
turtles = []
colors = ["red", "green", "coral", "purple", "cyan", "yellow", "blue"]


def make_race_line(x, y):
    line = t.Turtle()
    line.hideturtle()
    line.penup()
    line.setpos(x, y)
    line.pendown()
    line.setpos(x, -y)


def create_turtles():
    for i in range(len(colors)):
        turtle = t.Turtle()
        turtle.shape("turtle")
        turtle.color(colors[i])
        turtle.penup()
        turtle.setpos(-250, 150 - 50 * i)
        turtles.append(turtle)
        turtle.speed(0)


def start_race(x):
    while True:
        for turtle in turtles:
            turtle.forward(random.randint(1, 10))
            if turtle.xcor() >= x:
                return turtle.pencolor()


make_race_line(200, 200)
create_turtles()
guess_color = screen.textinput("Make your bet", "Which color turtle you think will win the race?\n""Options: 'red', "
                                                "'green', 'coral', 'purple', 'cyan', 'yellow', 'blue'\n")
winner_color = start_race(200)
if guess_color == winner_color:
    print(f"Congratulations!! You win :)\n{guess_color} turtle won the race")
else:
    print("Ahhhhhh!! You lose :(")
    print(f"The winner turtle was {winner_color} and your bet was on {guess_color}")
