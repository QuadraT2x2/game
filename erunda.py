import pygame
import sys
#изменения
pygame.init()
width = height = 110
margin = 25
columns = rows = 6
screen = pygame.display.set_mode(
    ((width * columns) + (margin * (columns + 1)), (height * rows) + margin * (rows + 1))
)
pygame.display.set_caption('Erunda')
background = pygame.image.load("bricks.jpg")
img = pygame.image.load("ayaya.jpg")
pygame.display.set_icon(img)

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)



mas = [[0] * columns for i in range(rows)]

while True:
    # добавить строчку, которая будет рисовать картинку.
    screen.blit(background, (0, 0))
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

    # обновляет картинку
    pygame.display.update()
