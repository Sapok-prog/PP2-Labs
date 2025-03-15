import pygame

pygame.init()
screen = pygame.display.set_mode((600 , 600))
x = 25
y = 25
done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and y >= 45:
            y -= 20
        elif event.key == pygame.K_DOWN and y <= 555:
            y += 20
        elif event.key == pygame.K_RIGHT and x <= 555:
            x += 20
        elif event.key == pygame.K_LEFT and x >= 45:
            x -= 20
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen , (255,0,0) , (x , y) , 25)
    pygame.display.flip()
    clock.tick(60)