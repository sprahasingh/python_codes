import turtle as t

pen = t.Turtle()
screen = t.Screen()

direction_heading = {'Right': 0, 'Left': 180, 'Up': 90, 'Down': 270}


def move_forward():
    pen.forward(10)


def move_backward():
    pen.left(180)
    pen.forward(10)


def clockwise():
    pen.right(10)


def counter_clockwise():
    pen.left(10)


def clear():
    t.resetscreen()


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
