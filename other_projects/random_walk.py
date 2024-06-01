import random
import turtle as t

tim = t.Turtle()
t.colormode(255)
angle = [90, 180, 270, 360]
tim.width(10)
tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for _ in range(500):
    tim.color(random_color())
    tim.setheading(random.choice(angle))
    if -100 <= tim.xcor() <= 100 and -100 <= tim.ycor() <= 100:
        tim.forward(30)
    else:
        tim.penup()
        tim.setpos(0, 0)
        tim.pendown()


screen = t.Screen()
screen.exitonclick()
