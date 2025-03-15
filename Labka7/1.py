import pygame 
import math
import time


pygame.init()
clock = pygame.time.Clock()
done = False
screen = pygame.display.set_mode((900 , 550))
angle = 0


#images
image_of_mousie = pygame.image.load(r"C:\Users\Amina\Downloads\clock.png")
right_arm = pygame.image.load(r"C:\Users\Amina\Downloads\rightarm.png")
left_arm = pygame.image.load(r"C:\Users\Amina\Downloads\leftarm.png")



background = pygame.transform.scale(image_of_mousie , (900 , 550))



while not done:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done =  True
    screen.blit(background , (0, 0))

    #time
    timing = time.localtime()
    minutes = timing.tm_min
    seconds = timing.tm_sec


     #Angles
    minute_angle = minutes * 6    + (seconds / 60) * 6   
    second_angle = seconds * 6 

    #Rotating
    rotated_minute = pygame.transform.rotate( pygame.transform.scale(right_arm, (800, 600)) , -minute_angle)
    new_rect = rotated_minute.get_rect(center=(450, 275))
    screen.blit(rotated_minute, new_rect)

    rotated_second = pygame.transform.rotate( pygame.transform.scale(left_arm, (40, 682)), -second_angle)
    ne_rect = rotated_second.get_rect(center=(450, 275))
    screen.blit(rotated_second, ne_rect)

    
    pygame.display.flip()
    clock.tick(60)