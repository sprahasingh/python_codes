import random
import turtle as t


t.colormode(255)
pen = t.Turtle()
pen.speed(0)

color_palette = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49),
                 (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120),
                 (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62)]


def set_pos(x_pos, y_pos):
    pen.penup()
    pen.setpos(x_pos, y_pos)
    pen.pendown()


def fill_color():
    pen.fillcolor(random.choice(color_palette))
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()


x = -300
y = -250
for _ in range(10):
    for _ in range(15):
        set_pos(x, y)
        fill_color()
        x += 50
    x = -300
    y += 50


screen = t.Screen()
screen.exitonclick()
