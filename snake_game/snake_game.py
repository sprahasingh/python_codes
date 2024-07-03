import turtle as t
import time
import random

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for pos in starting_positions:
    new_turtle = t.Turtle(shape="square")
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(pos)
    segments.append(new_turtle)

screen.update()

level = 0


def turn():
    screen.listen()
    if segments[0].heading() == 0 or segments[0].heading() == 180:
        screen.onkey(key="w", fun=move_north)
        screen.onkey(key="s", fun=move_south)
    else:
        screen.onkey(key="a", fun=move_west)
        screen.onkey(key="d", fun=move_east)


def move():
    while -300 < segments[0].xcor() < 300 and -300 < segments[0].ycor() < 300:
        screen.update()
        time.sleep(0.3)
        for segment in segments:
            segment.forward(20)
        turn()


def move_north():
    for i in range(0, len(segments)):
        screen.update()
        time.sleep(0.3)
        segments[i].setheading(90)
        for segment in segments:
            segment.forward(20)
    move()


def move_south():
    for i in range(0, len(segments)):
        screen.update()
        time.sleep(0.3)
        segments[i].setheading(270)
        for segment in segments:
            segment.forward(20)
    move()


def move_west():
    for i in range(0, len(segments)):
        screen.update()
        time.sleep(0.3)
        segments[i].setheading(180)
        for segment in segments:
            segment.forward(20)
    move()


def move_east():
    for i in range(0, len(segments)):
        screen.update()
        time.sleep(0.3)
        segments[i].setheading(0)
        for segment in segments:
            segment.forward(20)
    move()


def gen_ball():
    ball = t.Turtle(shape='circle')
    ball.color('white')
    ball.penup()
    x_cor = random.randint(-300, 300)
    y_cor = random.randint(-300, 300)
    pos_ball = (x_cor, y_cor)
    ball.goto(pos_ball)
    return pos_ball


def game():
    game_on = True
    gen_ball()
    while game_on:
        move()
        if not -300 < segments[0].xcor() < 300 and not -300 < segments[0].ycor() < 300:
            game_on = False


game()

screen.exitonclick()
