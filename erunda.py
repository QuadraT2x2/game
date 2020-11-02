import pygame
import sys

from screen_config import margin, width, height, columns, rows

pygame.init()


screenx = (width * columns) + (margin * (columns + 1))
screeny = (height * rows) + margin * (rows + 1)

screen = pygame.display.set_mode((screenx, screeny))

white_square = pygame.image.load("square_white.png")
white_square = pygame.transform.scale(white_square, (width, height))
bricks = pygame.image.load("bricks.jpg")
background = pygame.transform.scale(bricks, (screenx, screeny))
img = pygame.image.load("ayaya.jpg")
ayaya_image = pygame.transform.scale(img, (width, height))

pygame.display.set_icon(img)
pygame.display.set_caption('Erunda')

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)


def click_on_screen():
    x_mouse, y_mouse = pygame.mouse.get_pos()
    print(f'x = {x_mouse} y = {y_mouse}')
    column = min((columns - 1), x_mouse // (margin + width))
    row = min((rows - 1), y_mouse // (margin + height))
    print(f'row = {row} column = {column}')
    mas[row][column] ^= 1


mas = [[0] * columns for i in range(rows)]


def draw_image_in_square(square_row, square_column, image):
    square_x = margin + (margin + width) * square_column
    square_y = margin + (margin + height) * square_row
    screen.blit(image, (square_x, square_y))


while True:
    # добавить строчку, которая будет рисовать картинку.
    screen.blit(background, (0, 0))
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_on_screen()
    # Отрисовка экрана
    # рисует наши квадратики
    for row in range(rows):
        for column in range(columns):
            # передавали в функцию, рисующую в ряде или колонке текущий ряд, 
            # текущий столб,
            # тут только вызываем draw_image_in_square
            if mas[row][column] == 1:
                draw_image_in_square(row, column, ayaya_image)
            else:
                # вместо белого прямоугольника рисуем белую картинку
                draw_image_in_square(row, column, white_square)


    # обновляет картинку
    pygame.display.update()

