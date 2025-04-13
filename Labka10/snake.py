import pygame
import sys
import random
import psycopg2
from config import load_config

def insert_data(user, user_score, user_level):
    sql = "INSERT INTO SNAKE(username, score, level) VALUES(%s, %s, %s)"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as curr:
                curr.execute(sql, (user, user_score, user_level))
                conn.commit()
                return True
    except Exception as error:
        return False

def update_data(user, user_score, user_level):
    sql = "UPDATE SNAKE SET score = %s, level = %s WHERE username = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as curr:
                curr.execute(sql, (user_score, user_level, user))
                conn.commit()
    except Exception as error:
        print(error)

def get_user_data(user):
    sql = "SELECT score, level FROM SNAKE WHERE username = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as curr:
                curr.execute(sql, (user,))
                return curr.fetchone()
    except Exception as error:
        print(error)
        return None

# ----------------- GAME SETUP -----------------

pygame.init()
circle = 1
done = False
paused = False

pause_pic = pygame.image.load(r"C:\Users\Amina\Downloads\pause_game.jpg")
pause_pic = pygame.transform.scale(pause_pic, (600, 400))

def background(screen):
    for i in range((400//20)*20):
        for j in range((600//20)*20):
            color = (102,255,102) if (i + j) % 2 == 0 else (0,255,0)
            pygame.draw.rect(screen, color, (i * 20, j * 20, 20, 20))

shrift = pygame.font.Font(None, 50)
snake_pic = pygame.image.load(r"C:\Users\Amina\Downloads\best_snake.png")
snake_pic = pygame.transform.scale(snake_pic, (300,400))

screen = pygame.display.set_mode((600,400))
cell = 20
pygame.display.set_caption("Miras is Snake")
clock = pygame.time.Clock()

walls = [(x, y) for x in range(0, 600, cell) for y in range(0, 400, cell)
        if x == 0 or y == 0 or x == 600 - cell or y == 400 - cell]

snake = [(100,100), (80,100), (60,100)]
snake_dir = (cell, 0)

score = 0
level = 1
speed = 10
game_active = False

start_text = shrift.render("Press 'Space' to start", True, "White")
start_text_rec = start_text.get_rect(center = (400, 200))

class Nyama():
    def __init__(self):
        self.cell = 20
        self.food_pos = self.food()  
        self.time_of_apple = pygame.time.get_ticks()  
    
    def food(self):
        self.time_of_apple = pygame.time.get_ticks()
        while True:
            x = random.randint(1, (400//self.cell)-2) * self.cell
            y = random.randint(1, (400//self.cell)-2) * self.cell
            food_pos = (x, y)
            if food_pos not in snake and food_pos not in walls:
                return food_pos

AppleL = Nyama()
apples = AppleL.food()

# ----------------- GAME LOOP -----------------

start = input("want to start? 1(yes)/2(no): ")
if start != "1":
    sys.exit()

name = input("Enter your name: ")

if __name__ == '__main__':
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = not paused
                    elif event.key == pygame.K_UP and snake_dir != (0, cell):
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

        if game_active and not paused:
            head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
            snake.insert(0, head)

            background(screen)

            if head in snake[1:] or head[0] < 0 or head[1] < 0 or head[0] > 600 or head[1] > 400 or head in walls:
                game_active = False

            if head == apples:
                score += random.randint(10 , 50)
                AppleL.food_pos = AppleL.food()
                apples = AppleL.food()

                if score >= 30 * circle:
                    level += 1
                    speed += 3
                    circle += 1
            else:
                snake.pop()

            for i in walls:
                pygame.draw.rect(screen, "Orange", (i[0], i[1], cell, cell))

            for i in snake:
                pygame.draw.rect(screen, (0, 153, 0), (i[0], i[1], cell, cell))

            local_time = pygame.time.get_ticks()
            if local_time - AppleL.time_of_apple > 5000 and head != apples:
                AppleL.food_pos = AppleL.food()

            apples = AppleL.food_pos
            pygame.draw.rect(screen , "Red" , (apples[0], apples[1], cell, cell))

            screen.blit(shrift.render(f"Score: {score}", True, "White"), (10,10))
            screen.blit(shrift.render(f"Level {level}", True, "White"), (450, 10))
        elif paused:
            screen.blit(pause_pic, (0, 0))
        else:
            if score == 0 and not paused:
                screen.fill("Green")
                screen.blit(start_text, start_text_rec)
                screen.blit(snake_pic, (0,0))
            else:
                done = True

        pygame.display.update()
        clock.tick(speed)

    existing_user = get_user_data(name)
    if not existing_user:
        insert_data(name, score, level)
    else:
        print(f"Here you go again hihi , your current level - {existing_user[1]}")
        ansq = int(input("Do you want to update your score? 1(yes)/2(no): "))
        if ansq == 1:
            update_data(name, score, level)
        else:
            print("Okay, see you next time!")

    score = 0
    level = 0
