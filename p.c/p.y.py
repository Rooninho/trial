from turtle import *
from colorsys import *
setposition(50, -50)
speed(0)
bgcolor("blue")
pensize(3)
h=1
for i in range (10):
    for i in range(10):
        color(hsv_to_rgb(h, 1, 1))
        h += 0.004
        circle(50+i*5, 90)
        forward(60)
        left(80)
        right(90)
    hideturtle()
    rt(1)
done