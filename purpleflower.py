
#LeslieN
#2/11/25

#draw a nine petal flower

import turtle

screen = turtle.Screen()
screen.bgcolor("white")

flower = turtle.Turtle()
flower.shape("turtle")


def draw_petal():
    flower.color("purple")
    flower.circle(100,60)
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)


for _ in range(9):
    draw_petal()
    flower.left(40)

turtle.done()