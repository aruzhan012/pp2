import pygame
import random
from enum import Enum
from pygame import mixer


pygame.init()
pygame.mixer.init()

width = 800
height = 600
screen = pygame.display.set_mode((width,height))


background = pygame.image.load('C:\\Intel\\week9\\starfield.jpg')


sound = pygame.mixer.music.load('C:\\Intel\\week9\\battle-city_-tanchiki_-dend.mp3')
pygame.mixer.music.play()

#sound_bullet = pygame.mixer.Sound('C:\\Intel\\week9\\battle-city.mp3')
#sound_collision = pygame.mixer.Sound('C:\\Intel\\week9\\battle-city-sfx-7.mp3')
#sound_between_collision_and_game_over = pygame.mixer.Sound('C:\\Intel\\week9\\battle-city-sfx-2.mp3')



mainloop = True

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Tank:
    def __init__(self, x, y, speed, color, d_right=pygame.K_RIGHT, d_left=pygame.K_LEFT, d_up=pygame.K_UP, d_down=pygame.K_DOWN,d_pull=pygame.K_KP0):
        self.x = x
        self.y = y
        self.score=1
        self.speed = speed
        self.color = color
        self.width = 40
        self.direction = Direction.RIGHT

        self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT,
                    d_up: Direction.UP, d_down: Direction.DOWN}

        self.KEYPULL=d_pull
        
    def draw(self):
        tank_c = (self.x + int(self.width / 2), self.y + int(self.width / 2))
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.width), 2)
        pygame.draw.circle(screen, self.color, tank_c, int(self.width / 2))

        if self.direction == Direction.RIGHT:
            pygame.draw.line(screen, self.color, tank_c, (self.x + self.width + int(self.width / 2), self.y + int(self.width / 2)), 4)
            
        if self.direction == Direction.LEFT:
            pygame.draw.line(screen, self.color, tank_c, (
            self.x - int(self.width / 2), self.y + int(self.width / 2)), 4)

        if self.direction == Direction.UP:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width / 2), self.y - int(self.width / 2)), 4)

        if self.direction == Direction.DOWN:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width / 2), self.y + self.width + int(self.width / 2)), 4)


    def change_direction(self, direction):
        self.direction = direction

    def move(self):
        if self.direction == Direction.LEFT:
            self.x -= self.speed
        if self.direction == Direction.RIGHT:
            self.x += self.speed
        if self.direction == Direction.UP:
            self.y -= self.speed
        if self.direction == Direction.DOWN:
            self.y += self.speed
        self.draw()
    
    
class Pulya:
    def __init__(self,x=0,y=0,color=(0,0,0),direction=Direction.LEFT,speed=5):
        self.x=x
        self.y=y
        self.color=color
        self.speed=speed
        self.direction=direction
        self.status=True
        self.distance=0
        self.radius=5

    def move(self):
        if self.direction == Direction.LEFT:
            self.x -= self.speed
        if self.direction == Direction.RIGHT:
            self.x += self.speed
        if self.direction == Direction.UP:
            self.y -= self.speed
        if self.direction == Direction.DOWN:
            self.y += self.speed
        self.distance+=1
        if self.distance>(2*width):
            self.status=False
        self.draw()

    def draw(self):
        if self.status:
            pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
def give_coordinates(tank):
    if tank.direction == Direction.RIGHT:
        x=tank.x + tank.width + int(tank.width / 2)
        y=tank.y + int(tank.width / 2)

    if tank.direction == Direction.LEFT:
        x=tank.x - int(tank.width / 2)
        y=tank.y + int(tank.width / 2)

    if tank.direction == Direction.UP:
        x=tank.x + int(tank.width / 2)
        y=tank.y - int(tank.width / 2)

    if tank.direction == Direction.DOWN:
        x=tank.x + int(tank.width / 2)
        y=tank.y + tank.width + int(tank.width / 2)

    p=Pulya(x,y,tank.color,tank.direction)
    pulya.append(p)

def collision():
    #столкновение танка со стенкой
    for tank in tanks:
        if (tank.x<-41):
            tank.x=width
        elif tank.x>width:
            tank.x=-40
        if (tank.y<-41):
            tank.y=600
        elif tank.y>600:
            tank.y=-40

    #столкновение пули с танком
    for p in pulya:
        for tank in tanks:
            if (tank.x+tank.width+p.radius > p.x > tank.x - p.radius ) and ((tank.y+tank.width + p.radius > p.y > tank.y - p.radius)) and p.status==True:
                #sound_collision.play()
                p.color=(0,0,0)
                tank.score-=1
                p.status=False
                
                tank.x=random.randint(50,800-70)
                tank.y=random.randint(50,600-70)

    
def life():
    font = pygame.font.SysFont('Arial', 32) 
    score1 = tanks[0].score
    score2 = tanks[1].score
    res_p1 = font.render(str(score1), True, (255, 0, 0))
    res_p2 = font.render(str(score1), True, (255, 0, 0))
    res1 = font.render(str(score2),  True, (255, 255, 0))
    res2 = font.render(str(score2), True, (255, 255, 0))
    screen.blit(res_p1, (30,30))
    screen.blit(res_p2, (30, 30))
    screen.blit(res1, (750,30))

    if score1==0 or score2 == 0:
        
        
        screen.blit(res_p1, (230,500))
        screen.blit(res_p2, (230, 550))
        
        screen.blit(res1, (555,500))
        screen.blit(res2, (555,550))
        
        pygame.display.update()
        sound_game_over.play()
        time.sleep(5)
        
        pygame.quit()
        
mainloop = True
tank1 = Tank(300, 300, 2, (200,190,140),d_pull=pygame.K_KP_ENTER)
tank2 = Tank(100, 100, 2, (180,255,100), pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s,pygame.K_SPACE)

pulya1=Pulya()
pulya2=Pulya()

tanks = [tank1, tank2]
pulya = [pulya1,pulya2]

FPS = 30

clock = pygame.time.Clock()

while mainloop:
    mill = clock.tick(FPS)
    screen.fill((0, 0, 0))
    
    life()
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                quit()
            pressed = pygame.key.get_pressed()
            for tank in tanks:
                if event.key in tank.KEY.keys():
                    tank.change_direction(tank.KEY[event.key])
                
                if pressed[tank.KEYPULL]:
                    #sound_bullet.play()
                    give_coordinates(tank)
    for tank in tanks:                   
        tank.move()
    collision()

    for p in pulya:
        p.move()
    
    for tank in tanks:
        tank.draw() 
    pygame.display.flip()

pygame.quit()

        
