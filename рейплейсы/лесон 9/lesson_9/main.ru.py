import turtle
import random

screen = turtle.Screen()
t = turtle.Turtle()
t.pensize(70)
colors = ["red","orange","yellow","green","light blue","blue","purple"]

side = int(input("введи количество: "))
x = 80

for i in range(0, side):
    t.pencolor(random.choice(colors))
    t.fd(x)
    t.rt(360 / side)

screen.exitonclick()