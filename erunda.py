import pygame
import sys
#изменения
pygame.init()
screen = pygame.display.set_mode((1980, 980))
pygame.display.set_caption('Erunda')
img = pygame.image.load("ayaya.jpg")
pygame.display.set_icon(img)
width = height = 60
margin = 20

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

columns = 3
rows = 3


mas = [[0] * columns for i in range(rows)]

while True:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(f'x = {x_mouse} y = {y_mouse}')
            column = x_mouse // (margin + width)
            row = y_mouse // (margin + height)
            mas[row][column] ^= 1
    # Отрисовка экрана
    # рисует наши квадратики
    for row in range(rows):
        for column in range(columns):
            if mas[row][column] == 1:
                color = green
            else:
                color = white
            x = column * width + (column + 1) * margin
            y = row * height + (row + 1) * margin
            pygame.draw.rect(screen, color, (x, y, width, height))
    # добавить строчку, которая будет рисовать картинку.

    # обновляет картинку
    pygame.display.update()
