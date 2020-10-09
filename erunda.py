import pygame
import sys
#изменения
pygame.init()
screen = pygame.display.set_mode((980, 980))
pygame.display.set_caption('Erunda')
img = pygame.image.load("ayaya.jpg")
pygame.display.set_icon(img)
width = heigth = 300
margin = 20

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0] * 3 for i in range(3)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(f'x = {x_mouse} y = {y_mouse}')
            column = x_mouse // (margin + width)
            row = y_mouse // (margin + heigth)
            mas[row][column] ^= 1
    for row in range(3):
        for column in range(3):
            if mas[row][column] == 1:
                color = green
            else:
                color = white
            x = column * width + (column + 1) * margin
            y = row * heigth + (row + 1) * margin
            pygame.draw.rect(screen, color, (x, y, width, heigth))

    pygame.display.update()
