from turtle import *
import turtle
from random import randint
import time


def create_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

    # fill the above shape
    turtle.end_fill()
    # Reset the orientation of the turtle
    turtle.setheading(0)


def create_circle(oogway, x, y, radius, color):
    oogway.penup()
    oogway.color(color)
    oogway.fillcolor(color)
    oogway.goto(x, y)
    oogway.pendown()
    oogway.begin_fill()
    oogway.circle(radius)
    oogway.end_fill()

def christ():

    BG_COLOR = "#0080ff"
    oogway = Turtle()
    oogway.speed(6)
    screen = oogway.getscreen()
    screen.bgcolor(BG_COLOR)
    screen.title("Merry Christmas")
    screen.setup(width=1.0, height=1.0)

    y = -100
    create_rectangle(oogway, "red", -15, y-60, 30, 60)

    width = 240
    oogway.speed(6)
    while width > 10:
        width = width - 10
        height = 10
        x = 0 - width/2
        create_rectangle(oogway, "green", x, y, width, height)
        y = y + height

    oogway.speed(6)
    oogway.penup()
    oogway.color('yellow')
    oogway.goto(-20, y+10)
    oogway.begin_fill()
    oogway.pendown()
    for i in range(5):
        oogway.forward(40)
        oogway.right(144)
    oogway.end_fill()

    tree_height = y + 40

    create_circle(oogway, 230, 180, 60, "white")
    create_circle(oogway, 220, 180, 60, BG_COLOR)

    oogway.speed(10)
    number_of_stars = randint(20,30)

    for _ in range(0,number_of_stars):
        x_star = randint(-(screen.window_width()//2),screen.window_width()//2)
        y_star = randint(tree_height, screen.window_height()//2)
        size = randint(5,20)
        oogway.penup()
        oogway.color('white')
        oogway.goto(x_star, y_star)
        oogway.begin_fill()
        oogway.pendown()
        for i in range(5):
            oogway.forward(size)
            oogway.right(144)
        oogway.end_fill()

    # print greeting message
    oogway.speed(1)
    oogway.penup()
    msg = "Merry Christmas to ALL"
    oogway.goto(0, -200) 
    oogway.color("white")
    oogway.pendown()
    oogway.write(msg, move=False, align="center", font=("Arial", 15, "bold"))
    oogway.hideturtle()
    time.sleep(4)
    
    turtle.bye()
    return 'Done'


if __name__ ==  '__main__':
        christ()



