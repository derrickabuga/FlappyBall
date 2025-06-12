import pygame
import sys

#INITIALIZE PYGAME
pygame.init()

#SET SCREEN DIMENSIONS
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))      #CREATE GAME WINDOW
pygame.display.set_caption("FLAPPY BALL")       #WINDOW TITLE

#CLOCK TO CONTROL FRAME RATE
clock = pygame.time.Clock()
FPS = 60

#COLOURS TO USE
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 0, 0)

#BALL PROPERTIES
ball_radius = 20
ball_position_x = 100       #Horizontal position of ball stays the same
ball_position_y = SCREEN_HEIGHT // 2        #Ball initially at center of screen
ball_velocity = 0
gravity = 0.5
jump_strength = -10


#GAME LOOP
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Jump when space bar is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball_velocity = jump_strength

    ball_velocity += gravity
    ball_position_y += ball_velocity

    #Keep ball from falling off-screen
    if ball_position_y + ball_radius > SCREEN_HEIGHT:
        ball_position_y = SCREEN_HEIGHT - ball_radius
        ball_velocity = 0

    #Display screen and draw ball
    screen.fill(BLUE)
    pygame.draw.circle(screen, RED, (ball_position_x, int(ball_position_y)), ball_radius)

    pygame.display.flip()

pygame.quit()
sys.exit()