import pygame
pygame.init()
import random
from colorsys import*
from turtle import*
bgcolor="white"
pygame.init()
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the Ball")
paddle_width, paddle_height = 100, 10
paddle_x = width // 2 - paddle_width // 2
paddle_y =height - 30
paddle_speed = 7
ball_radius =10
ball_x =random.randint(ball_radius, width - ball_radius)
ball_y = 0
ball_speed = 4
score=0
font = pygame.font.SysFont(None, 36)
running=True
clock= pygame.time.Clock()
while running:
    screen.fill("yellow") 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
    keys = pygame.key.get_pressed()        
    if keys[pygame.K_LEFT] and paddle_x> 0:
        paddle_x-= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x<width -paddle_x:
        paddle_x += paddle_speed
    ball_y += ball_speed
    if (paddle_y<ball_y + ball_radius< paddle_y + paddle_height and paddle_x< ball_x<paddle_x +paddle_width):
        score += 1
        ball_y = 1
        ball_x = 1
random.randint(ball_radius, width-ball_radius)
if ball_y >height:
    ball_y=0
    ball_x=1
random.randint(ball_radius, width-ball_radius)
pygame.draw.rect(screen, "blue",(paddle_x, paddle_y, paddle_width,paddle_height))
pygame.draw.circle(screen, "red",(ball_x,ball_y), ball_radius)
score_text = font.render(f"Score:{score}", True, (0, 0, 0))
screen.blit(score_text, (10, 10))
pygame.display.flip()
clock.tick(60)
pygame.quit()

 