#imports
import pygame
from pygame.locals import *
from random import randint
import time
pygame.init()
#epic music 
pygame.mixer.music.load(r"C:\Users\Amina\Downloads\Sean Paul - Temperature (Album Version).mp3")
pygame.mixer.music.play()

#main variables to use
done =  False
clock = pygame.time.Clock()
speed = 5 
score = 0
count_of_coins = 0

#background
background = pygame.image.load(r"C:\Users\Amina\Downloads\back.png")
background = pygame.transform.scale(background , (400 , 600))

#game over
game_over = pygame.image.load(r"C:\Users\Amina\Downloads\crash.jpg")
game_over = pygame.transform.scale(game_over , (400 , 600))


#colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)

#fonts
font = pygame.font.SysFont("Verdana" , 50)
GAME_TOCHNO_OVER = font.render("GAME OVER" , True , BLACK)
WE_DID_IT = font.render("SCORE:" , True ,  BLACK)
BOHACH = font.render("COINS:" , True , YELLOW)

#screen
screen = pygame.display.set_mode((400 , 600))
pygame.display.set_caption("Racer")
screen.fill(WHITE)

#creating enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Amina\Downloads\bluee_car.png")
        self.image = pygame.transform.scale(self.image , (50 , 100))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40 , 360) , -100)

    def move(self):
        global score
        self.rect.move_ip(0 , 8)
        if (self.rect.bottom > 710):
            score += 1
            self.rect.top = -100
            self.rect.center = (randint(30, 370), -100)

    def draw(self, surface):
        surface.blit(self.image , (self.rect))

#creating us
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Amina\Downloads\norm_car.png")
        self.image = self.image = pygame.transform.scale(self.image , (70 , 100))
        self.rect = self.image.get_rect()
        self.rect.center = (200 , 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5 , 0)
        if self.rect.right < 400:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5 , 0)

    def draw(self , surface):
        surface.blit(self.image , self.rect)

#creating coins
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load(r"C:\Users\Amina\Downloads\coin.png")
        self.image = pygame.transform.scale(self.image , (50 , 50))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(10 , 390) , -50)
    def move(self):
        self.rect.move_ip(0 , 8)
        if (self.rect.bottom > 710):
            self.rect.top = -100
            self.rect.center = (randint(10, 390), -50)
    def draw(self, surface):
        surface.blit(self.image , (self.rect))

#setting up spirits(objects)
P1 = Player()
E1 = Enemy()
C1 = Coins()

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED , 1000)

#Game Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if event.type == INC_SPEED:
        speed += 5 #add speed for game

    screen.blit(background , (0 , 0))
    P1.move()
    E1.move()

    denga = font.render(str(count_of_coins) , True , YELLOW) #display count of coins
    screen.blit(denga , (10 , 50))
    scores = font.render(str(score) , True , WHITE) #display actual score
    screen.blit(scores , (10 , 5))

    P1.draw(screen)
    E1.draw(screen)

    if P1.rect.colliderect(E1.rect):
        pygame.mixer.music.stop()
        pygame.mixer.Sound(r"C:\Users\Amina\Downloads\quaquaqua.mp3").play()
        time.sleep(0.5)

        screen.blit(game_over , (0 , 0))
        screen.blit(WE_DID_IT , (20 , 400))
        screen.blit(scores , (220, 400))
        screen.blit(BOHACH , (20 , 450))
        screen.blit(denga , (220 , 450))
        screen.blit(GAME_TOCHNO_OVER , (20 , 350))

        pygame.display.update()
        
        time.sleep(5)
        done = True #we cancel program

    if P1.rect.colliderect(C1.rect):
        pygame.mixer.Sound(r"C:\Users\Amina\Downloads\coin_nya.mp3").play()
        count_of_coins += 1  #collect coins and add new cordinate 
        C1.rect.top = -50  
        C1.rect.center = (randint(10, 390), -50) 
    else:
        C1.move()
        C1.draw(screen)
    

    pygame.display.flip()
    clock.tick(60)

    