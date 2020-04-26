import pygame
import sys
import time
import random
 
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game")
 
red = pygame.Color(255, 6, 7)
green = pygame.Color(9, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)
yellow = pygame.Color(255,255,204)
 
clock = pygame.time.Clock()
 
d = 10
snakePos = [100, 50]
snakeBody = [[100, 30], [60, 50], [80, 50]]
foodPos = [400, 50]
food = True
direction = 'RIGHT'
changeto = ''
score = 0
 
 
 
def gameOver():
    myFont = pygame.font.SysFont('Arial', 36)
    GOsurf = myFont.render("Game Over", True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (400, 300)
    screen.blit(GOsurf, GOrect)
    showScore(0)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()
 
 
def showScore(choice=1):
    SFont = pygame.font.SysFont('monaco', 32)
    Ssurf = SFont.render("Score  :  {0}".format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (400, 200)
    screen.blit(Ssurf, Srect)
 
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
 
 
    if changeto == 'RIGHT' and direction != 'LEFT':
        direction = changeto
    if changeto == 'LEFT' and direction != 'RIGHT':
        direction = changeto
    if changeto == 'UP' and direction != 'DOWN':
        direction = changeto
    if changeto == 'DOWN' and direction != 'UP':
        direction = changeto
 
 
    if direction == 'RIGHT':
        snakePos[0] += d
    if direction == 'LEFT':
        snakePos[0] -= d
    if direction == 'DOWN':
        snakePos[1] += d
    if direction == 'UP':
        snakePos[1] -= d
 
 
    snakeBody.insert(0, list(snakePos))
    if snakePos == foodPos:
        food = False
        score += 1
    else:
        snakeBody.pop()
    if food == False:
        foodPos = [random.randrange(1, 800 // 10) * d, random.randrange(1, 600 // 10) * d]
        food = True
 
 
    screen.fill(yellow)
    for pos in snakeBody:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], d, d))
    pygame.draw.rect(screen, brown, pygame.Rect(foodPos[0], foodPos[1], d, d))
 
 
    if snakePos[0] >= 800 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] >= 600 or snakePos[1] < 0:
        gameOver()
 
 
    for block in snakeBody[1:]:
        if snakePos == block:
            gameOver()
            
    showScore()
    pygame.display.flip()
    clock.tick(20) 