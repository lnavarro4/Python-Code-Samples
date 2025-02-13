
#LeslieN
#2/11/25

#draws polygon based on description given

import turtle

def polygon(sides, length, line, fill):
    screen = turtle.Screen()
    screen.bgpic("white")

    polygon_turtle = turtle.Turtle()

    polygon_turtle.pencolor(line)
    polygon_turtle.fillcolor(fill)

    polygon_turtle.begin_fill()

    for _ in range(sides):
        polygon_turtle.forward(length)
        polygon_turtle.left(360 / sides)

    polygon_turtle.end_fill()

    polygon_turtle.hideturtle()
    turtle.done()


sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length of each side: "))
line = input("Enter the color of the line: ")
fill = input("Enter the fill color: ")

polygon(sides, length, line, fill)

