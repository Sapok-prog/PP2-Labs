import pygame

#start
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))
done = False

#images 
album = pygame.image.load(r"C:\Users\Amina\Downloads\NewJeans_-_Get_Up.png")
album = pygame.transform.scale(album, (400, 400))

play = pygame.image.load(r"C:\Users\Amina\Downloads\play.png")
play = pygame.transform.scale(play, (120, 120))

pause = pygame.image.load(r"C:\Users\Amina\Downloads\pause.png")
pause = pygame.transform.scale(pause, (120, 120))

next_song = pygame.image.load(r"C:\Users\Amina\Downloads\next.png")
next_song = pygame.transform.scale(next_song, (200, 200))
bigger_next = pygame.transform.scale(next_song, (220, 220))

back_song = pygame.image.load(r"C:\Users\Amina\Downloads\back.png")
back_song = pygame.transform.scale(back_song, (200, 200))
bigger_back = pygame.transform.scale(back_song, (220, 220))

#extra values to work with buttons
count = 0
is_paused = False
is_next = False
is_back = False
next_timer = 0
back_timer = 0

songs_yasss = [
    r"C:\Users\Amina\Downloads\NewJeans - Get Up.mp3",
    r"C:\Users\Amina\Downloads\NewJeans - Super Shy.mp3",
    r"C:\Users\Amina\Downloads\NewJeans - ASAP.mp3",
    r"C:\Users\Amina\Downloads\newjeans-eta.mp3",
    r"C:\Users\Amina\Downloads\NewJeans - Cool With You.mp3",
    r"C:\Users\Amina\Downloads\NewJeans - New Jeans.mp3"
]

pygame.mixer.music.load(songs_yasss[count])
pygame.mixer.music.play()

while not done:
    screen.fill((255, 100, 180))
    screen.blit(album, (100, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    is_paused = True
                    pygame.mixer.music.pause()
                else:
                    is_paused = False
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                count += 1
                if is_paused:
                    is_paused = False
                pygame.mixer.music.load(songs_yasss[count])
                pygame.mixer.music.play()
                is_next = True
                next_timer = pygame.time.get_ticks()  
            elif event.key == pygame.K_LEFT:
                count = (count - 1) % len(songs_yasss)
                pygame.mixer.music.load(songs_yasss[count])
                pygame.mixer.music.play()
                is_back = True
                back_timer = pygame.time.get_ticks()

    #pause and play
    if is_paused:
        screen.blit(play, (237, 455))
    else:
        screen.blit(pause, (237, 455))

    
    #next and back
    current_time = pygame.time.get_ticks()
    if is_next and current_time - next_timer < 250:  
        screen.blit(bigger_next, (353, 415))
    else:
        screen.blit(next_song, (355, 420))
        is_next = False  

    if is_back and current_time - back_timer < 250:
        screen.blit(bigger_back, (35, 410))
    else:
        screen.blit(back_song, (38, 415))
        is_back = False

    pygame.display.flip()
    clock.tick(60)

