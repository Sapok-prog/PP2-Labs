import pygame
from math import sqrt

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
prevX = 0
prevY = 0
prevX1 = -1
prevY1 = -1
currentX1 = -1
currentY1 = -1

#делаем экран
color = (255, 255, 255)
screen.fill((0, 0, 0))

isMouseDown = False
mode = 0  #0 ручка 1 прямоугольник 2 круг 3 ластик

running = True
while running:
    currentX = prevX
    currentY = prevY

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Обработка нажатий мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                isMouseDown = True
                currentX1, currentY1 = event.pos
                prevX1, prevY1 = event.pos
                temp_surface = screen.copy()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                isMouseDown = False

        if event.type == pygame.MOUSEMOTION:
            currentX, currentY = event.pos

        #Смена цвета
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
            elif event.key == pygame.K_w:
                color = (255, 255, 255)

            #Переключение режимов
            elif event.key == pygame.K_1:
                mode = 1 #Прямоугольник
            elif event.key == pygame.K_2:
                mode = 2 #Круг
            elif event.key == pygame.K_3:
                mode = 3 #Ластик
            elif event.key == pygame.K_4:
                mode = 4 #Квадрат
            elif event.key == pygame.K_5:
                mode = 5 #Равнобедренный Треугольник
            elif event.key == pygame.K_6:
                mode = 6 #Правильный треугольник
            elif event.key == pygame.K_7:
                mode = 7 #Ромб
            elif event.key == pygame.K_0:
                mode = 0 #Перо


    #Перо
    if isMouseDown and mode == 0:
        pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY))

    #Прямоугольник
    if isMouseDown and mode == 1 and prevX1 != -1 and prevY1 != -1:
        screen.blit(temp_surface, (0, 0))
        pygame.draw.rect(screen, color, (min(prevX1, currentX), min(prevY1, currentY), abs(currentX - prevX1), abs(currentY - prevY1)), 1)

    #Круг
    if isMouseDown and mode == 2 and prevX1 != -1 and prevY1 != -1:
        screen.blit(temp_surface, (0, 0))
        centerX = (prevX1 + currentX) // 2
        centerY = (prevY1 + currentY) // 2
        radius = int(sqrt((currentX - prevX1)**2 + (currentY - prevY1)**2) // 2)

        pygame.draw.circle(screen, color, (centerX, centerY), radius, 1)

    #Ластик
    if isMouseDown and mode == 3:
        pygame.draw.line(screen, (0, 0, 0), (prevX, prevY), (currentX, currentY), 30)

    #Квадрат
    if isMouseDown and mode == 4 and prevX1 != - 1 and prevY1 != -1:
        screen.blit(temp_surface, (0, 0))
        side_length = max(abs(currentX - prevX1), abs(currentY - prevY1))
        top_left_x = min(prevX1, currentX) if currentX >= prevX1 else prevX1 - side_length
        top_left_y = min(prevY1, currentY) if currentY >= prevY1 else prevY1 - side_length

        pygame.draw.rect(screen, color, (top_left_x, top_left_y, side_length, side_length), 1)

    # Равнобедренный треугольник
    if isMouseDown and mode == 5 and prevX1 != -1 and prevY1 != -1:
        screen.blit(temp_surface, (0, 0))

        # Фиксируем основание
        left_x = min(prevX1, currentX)  # Левая нижняя точка
        right_x = max(prevX1, currentX)  # Правая нижняя точка

        # Высота равнобедренного треугольника (от основания до currentY)
        height = abs(currentY - prevY1)

        # Координаты вершин
        point1 = (left_x, prevY1)  # Левая нижняя вершина
        point2 = (right_x, prevY1)  # Правая нижняя вершина
        point3 = ((left_x + right_x) // 2, currentY)  # Верхняя вершина (движется мышью!)

        pygame.draw.polygon(screen, color, [point1, point2, point3], 1)

    #Правильный треугольник
    if isMouseDown and mode == 6 and prevX1 != -1 and prevY1 != -1:
        screen.blit(temp_surface, (0, 0))

        # Определяем длину стороны треугольника
        side_length = max(abs(currentX - prevX1), abs(currentY - prevY1))

        # Вычисляем высоту треугольника
        height = int((sqrt(3) / 2) * side_length)

        # Нижние две точки (основание)
        left_x = prevX1
        right_x = prevX1 + side_length
        bottom_y = prevY1

        # Верхняя вершина
        top_x = prevX1 + side_length // 2
        top_y = prevY1 - height

        # Координаты вершин
        point1 = (left_x, bottom_y)  # Левая нижняя точка
        point2 = (right_x, bottom_y)  # Правая нижняя точка
        point3 = (top_x, top_y)  # Верхняя точка

        pygame.draw.polygon(screen, color, [point1, point2, point3], 1)

    #Ромб 
    if isMouseDown and mode == 7 and prevX1 != -1 and prevY1 != -1:
        screen.blit(temp_surface, (0, 0))

        # Размер ромба (по ширине и высоте)
        half_width = abs(currentX - prevX1) // 2
        half_height = abs(currentY - prevY1) // 2

        # Центр ромба
        center_x = (prevX1 + currentX) // 2
        center_y = (prevY1 + currentY) // 2

        # Вершины ромба
        point1 = (center_x, center_y - half_height)  # Верхняя вершина
        point2 = (center_x + half_width, center_y)  # Правая вершина
        point3 = (center_x, center_y + half_height)  # Нижняя вершина
        point4 = (center_x - half_width, center_y)  # Левая вершина

        pygame.draw.polygon(screen, color, [point1, point2, point3, point4], 1)


    prevX = currentX
    prevY = currentY

    pygame.display.flip()
    clock.tick(45)

pygame.quit()