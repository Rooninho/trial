import pygame
from random import randint
from colorsys import*
from turtle import*
running=False
bgcolor("black")
title("SNAKE GAME")
Screen=Screen()
Screen.setup(width=500, height=500)
Screen.tracer(0)
#snake
snake=[]
lenght= 5
direction="Right"
#food
food=Turtle("circle")
food.color("red")
food.penup()
food.speed(-6)
food.goto(randint(-300, 300),
randint(-300, 300))
#score
score=0
high_score=0
score_writer=Turtle()
score_writer.hideturtle()
score_writer.color()
score_writer.penup()
score_writer.goto(0, 300)
score_writer.write(f"Score: {score} High Score:{high_score}", align="center", font=("courier", 18, "normal"))
#body
for i in range(lenght):
    segment=Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(-20*i, 0)
    snake.append(segment)
#movement
def go_up():
    global direction
    if direction !="Down":
        direction="Up"
def go_down():
    global direction
    if direction !="Up":
        direction="Down"
def go_left():
    global direction
    if direction !="Right":
        direction="Left"
def go_right():
    global direction
    if direction !="Left":
        direction="Right"
def start_game():
    global direction
    if direction=="stop":
        direction="Right"
        move()
Screen.onkey(start_game, "space")
Screen.listen()
Screen.onkey(go_up, "Up")
Screen.onkey(go_down, "Down",)
Screen.onkey(go_left, "Left",)
Screen.onkey(go_right, "Right")
#movement by snake
def move():
    global score, high_score
    x=snake[0].xcor()
    y=snake[0].ycor()
    if direction=="Up":
        snake[0].sety(y+20)
    if direction=="Down":
        snake[0].sety(y-20)
    if direction=="Left":
        snake[0].setx(x-20)
    if direction=="Right":
        snake[0].setx(x+20)
#snake move body segments
    for i in range(len(snake)-1, 0, -1):
        x=snake[i-1].xcor()
        y=snake[i-1].ycor()
        snake[i].goto(x, y)
#mongo move
    head=snake[0]
    if direction=="up":
        head.sety(head.ycor() + 20)
    if direction=="down":
        head.sety(head.ycor() - 20)
    if direction=="left":
        head.setx(head.xcor() - 20)
    if direction=="right":
        head.setx(head.xcor() + 20)

#collide with kiroma
    if snake[0].distance(food) <20:
        new_segment=Turtle("square")
        new_segment.penup()
        tail= snake[-1]
        new_segment.goto(tail.xcor(),tail.ycor())
        snake.append(new_segment)
        food.goto(randint(-300, 300), randint(-300, 300))
        score+=10
        if score> high_score:
            high_score=score
        score_writer.clear()
        score_writer.write(f"score:{score} High Score:{high_score}", align="center", font=("courier", 18, "normal"))
#collide na ukuta
    if abs(head.xcor())>=300 or abs(head.ycor())>=-300:
        reset_game()
#collide na mwili yake
    for segment in snake[1:]:
        if head.distance(segment)<20:
         reset_game()
    for i, segment in enumerate(snake):
        h=i / len(snake)
        r, g, b=hsv_to_rgb(h, 1.0, 1.0)
        segment.color((r, g, b))
    Screen.update()
    Screen.ontimer(move, 100)
def reset_game():
    global score
    score=0
    score_writer.clear()
    score_writer.write("Score: {score} High score: {high_score}",align="center", font=("Courier", 18, "normal"))
    for segment in snake[:1]:
        segment.goto(1000, 1000)
    del snake[1:]
    snake[0].goto(0, 0)
    global direction
    direction="stop" 
    running=False
#start game loop
running=True
move()
Screen.mainloop()


    


    

    
