import pygame
import sys
import random

pygame.init()
circle = 1

#doing back as chess desk
def background(screen): 
    for i in range((400//20)*20):
        for j in range((600//20)*20):
            if (i + j) % 2 == 0:
                color = (102,255,102)
            else:
                color = (0,255,0)

            pygame.draw.rect(screen, color, (i * 20, j * 20, 20, 20))


shrift = pygame.font.Font(None, 50)
snake_pic = pygame.image.load(r"C:\Users\Amina\Downloads\best_snake.png")
snake_pic = pygame.transform.scale(snake_pic, (300,400))

screen = pygame.display.set_mode((600,400))
cell = 20 #size of one snake's step
pygame.display.set_caption("Miras is Snake")

clock = pygame.time.Clock()
walls = [(x, y) for x in range(0, 600, cell) for y in range(0, 400, cell)
        if x == 0 or y == 0 or x == 600 - cell or y == 400 - cell] #makes wall 

snake = [(100,100), (80,100), (60,100)] #snake's beginning body
snake_dir = (cell, 0)  #its direction where our snake's head will move on

score = 0
speed = 10 
level = 1

game_active = False

start_text = shrift.render("Press 'Space' to start", True, "White")
start_text_rec = start_text.get_rect(center = (400, 200))


#Food's class
class Nyama():
    def __init__(self):
        self.cell = 20
        self.food_pos = self.food()  
        self.time_of_apple = pygame.time.get_ticks()  
    
    def food(self):
        self.time_of_apple = pygame.time.get_ticks() #count miliseconds of how much time food is standing in game_station
        while True:
            x = random.randint(1, (400//self.cell)-2) * self.cell
            y = random.randint(1, (400//self.cell)-2) * self.cell
            food_pos = (x, y) #placement of food
            if food_pos not in snake and food_pos not in walls:
                return food_pos

AppleL = Nyama()
apples = AppleL.food()

#Run Game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN: #turn snake's direction depend on keyboard
                if event.key == pygame.K_UP and snake_dir != (0, cell):
                    snake_dir = (0, -cell)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -cell):
                    snake_dir = (0, cell)
                elif event.key == pygame.K_LEFT and snake_dir != (cell, 0):
                    snake_dir = (-cell, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-cell, 0):
                    snake_dir = (cell, 0)
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True 
                snake = [(100,100), (80,100), (60,100)]
                snake_dir = (cell, 0)

                score = 0
                speed = 10 
                level = 1
                circle = 1

                apples = AppleL.food()

    if game_active: 
        head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1]) 
        snake.insert(0, head) #insert new element as head and count of elements lenght(snake)+1 NOW

        background(screen)
        if head in snake[1:] or head[0] < 0 or head[1] < 0 or head[0] > 600 or head[1] > 400:
            game_active = False

        if head in walls:
            game_active = False

        if head == apples: #if we get apple apple 
            score += random.randint(10 , 50) #add random size of apple
            AppleL.food_pos = AppleL.food()
            apples = AppleL.food() #and add new cordinate of apple
            
            if score >= 30 * circle:
                level += 1
                speed += 3
                circle += 1

        else:
            snake.pop() #till the moment we eat apple the last element is popped


        for i in walls:
            pygame.draw.rect(screen, "Orange", (i[0], i[1], cell, cell))

        for i in snake:
            pygame.draw.rect(screen, (0, 153, 0), (i[0], i[1], cell, cell))

        local_time = pygame.time.get_ticks()
        if local_time - AppleL.time_of_apple > 5000 and head != apples:
            AppleL.food_pos = AppleL.food()

        apples = AppleL.food_pos
        
        
        pygame.draw.rect(screen , "Red" , (apples[0], apples[1], cell, cell))

        score_text = shrift.render(f"Score: {score}", True, "White")
        level_text = shrift.render(f"Level {level}", True, "White")
        screen.blit(score_text, (10,10))
        screen.blit(level_text, (450, 10))
    
    else: 
        screen.fill("Black")
        game_over = shrift.render("GAME OVER", True, "White")
        game_over_rec = game_over.get_rect(center = (300, 150))
        my_score = shrift.render(f"Your score: {score}", True, "White")
        my_score_rec = my_score.get_rect(center = (300,250))

        if score == 0:
            screen.fill("Green")
            screen.blit(start_text, start_text_rec)
            screen.blit(snake_pic, (0,0))

        else:
            screen.blit(game_over, game_over_rec)
            screen.blit(my_score, my_score_rec)

    

    pygame.display.update()
    clock.tick(speed)