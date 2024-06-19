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
        turtle = t.Turtle(shape="turtle")
        turtle.color(colors[i])
        turtle.penup()
        turtle.setpos(-230, 150 - 50 * i)
        turtles.append(turtle)
        turtle.speed(0)


def start_race(x):
    while True:
        for turtle in turtles:
            turtle.forward(random.randint(1, 10))
            if turtle.xcor() >= x:
                return turtle.pencolor()


screen.setup(width=500, height=400)
make_race_line(200, 170)
create_turtles()
guess_color = screen.textinput("Make your bet", "Which color turtle you think will win the race?\n""Options: 'red',"
                                                "'green', 'coral', 'purple', 'cyan', 'yellow', 'blue'\n").lower()
while True:
    if guess_color not in colors:
        guess_color = screen.textinput("Enter valid color",
                                       "Which color turtle you think will win the race?\n""Options: 'red',"
                                       "'green', 'coral', 'purple', 'cyan', 'yellow', 'blue'\n").lower()
    else:
        break
winner_color = start_race(200)
if guess_color == winner_color:
    print(f"Congratulations!! You win :)\n{guess_color.upper()} turtle won the race")
else:
    print("Ahhhhhh!! You lose :(")
    print(f"The winner turtle was {winner_color.upper()} and your bet was on {guess_color.upper()}")
screen.exitonclick()
