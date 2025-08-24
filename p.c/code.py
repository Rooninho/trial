from turtle import*
from colorsys import*
bgcolor("black")
speed=0
pensize=4
setposition(30, -30)
n=1
f=1
for i in range(20):
    for i in range (30):
      color(hsv_to_rgb(n, f, 1))
      n += 0.004
      circle(3, 4, 6)
      forward(80)
      left(80)
      right(20)
      rt(3)
    hideturtle()
done
            