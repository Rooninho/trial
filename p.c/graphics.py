from turtle import * 
from colorsys import*
speed=5
bgcolor("black")
pensize(1)
h=1
for i in range (50):
        color(hsv_to_rgb(h, 1, 1))
        h += 0.004
        circle(50+i*5, 50)
        forward(90)
        left(80)
        def hideturtle():
                print()
        
hideturtle()
rt(1)
done




