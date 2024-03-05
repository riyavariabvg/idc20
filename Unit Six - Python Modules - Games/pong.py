import random
import sys
import pygame
import time

pygame.init()

# set up the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

player1_score = 0
player2_score = 0 
font = pygame.font.SysFont(None, 36)


# define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# define the game variables 
clock = pygame.time.Clock()
paddle2_y = 0
paddle1_y = 0  
ball_x_speed = random.choice([-10,-10])
ball_y_speed = random.choice([-9,-9])
paddle_speed = 10
ball_x = WIDTH//2
ball_y = HEIGHT//2
radius = 15

# game loop 
running = True
while running:
    screen.fill(WHITE)
    paddle1_rect = pygame.Rect(15, paddle1_y, 30, 100)
    paddle2_rect = pygame.Rect(WIDTH - 45, paddle2_y, 30, 100)
    paddle1 = pygame.draw.rect(screen, BLACK, (15, paddle1_y, 30, 100))
    paddle2 = pygame.draw.rect(screen, BLACK, (WIDTH - 45, paddle2_y, 30, 100))
    ball = pygame.draw.circle(screen, RED, (ball_x, ball_y), radius)

    # handle events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    clock.tick(60)  # set the frame rate to 60 frames per second

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: 
        paddle2_y -= paddle_speed
        paddle2_y = max(paddle2_y, 0)  
    if keys[pygame.K_DOWN]:
        paddle2_y += paddle_speed
        paddle2_y = min(paddle2_y, HEIGHT-100)  
    if keys[pygame.K_w]:
        paddle1_y -= paddle_speed
        paddle1_y = max(paddle1_y, 0)  
    if keys[pygame.K_s]:
        paddle1_y += paddle_speed
        paddle1_y = min(paddle1_y, HEIGHT-100)  
    
    ball_x +=ball_x_speed
    ball_y+=ball_y_speed
    ball_rect = pygame.Rect(ball_x - radius, ball_y - radius, 2*radius, 2*radius)

    if ball_rect.colliderect(paddle2_rect):
        ball_x_speed = ball_x_speed*-1
    
    elif ball_rect.colliderect(paddle1_rect):
        ball_x_speed = abs(ball_x_speed)
         
    elif ball_y <= 1:
        ball_y_speed = ball_y_speed*-1
    
    elif ball_y >= HEIGHT:
        ball_y_speed = -1*ball_y_speed
    
    elif ball_x >= WIDTH:
        player1_score+=1
        ball_x = WIDTH//2
        ball_y = HEIGHT//2
        ball_x_speed = random.choice([-10,-10])
        ball_y_speed = random.choice([-9,-9])

    
    elif ball_x <= 0:
        player2_score+=1
        ball_x = WIDTH//2
        ball_y = HEIGHT//2
        ball_x_speed = random.choice([-10,-10])
        ball_y_speed = random.choice([-9,-9])

    player1_score_text = font.render(f"Player 1: {player1_score}", True, BLACK)
    screen.blit(player1_score_text, (200, 10))
    player2_score_text = font.render(f"Player 2: {player2_score}", True, BLACK)
    screen.blit(player2_score_text, (400, 10))

    if player1_score == 10 or player2_score == 10:
        if player1_score > player2_score:
            winner = "Player 1"
        else:
            winner = "Player 2"
        screen.fill(BLACK)
        endgame = font.render(f"WINNER: {winner}", True, WHITE)
        screen.blit(endgame, (WIDTH//2-80, HEIGHT//2))
        running = False 

    pygame.display.flip()
    if running == False:
        time.sleep(5)


pygame.quit()
sys.exit()