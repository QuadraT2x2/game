import pygame
import sys

from graphics_utils import draw_image_in_square
from images import kitten, dog, chiken, dragon, tiger, ayaya, background, white_square
from screen_config import margin, width, height, columns, rows, screen

pygame.init()

#my_list = [kitten, dog, chiken, dragon, tiger, ayaya]

pygame.display.set_icon(ayaya)
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
    draw_image_in_square(0, 0, kitten)
    draw_image_in_square(0, 1, dog)
    draw_image_in_square(0, 2, chiken)
    draw_image_in_square(0, 3, dragon)
    draw_image_in_square(0, 4, tiger)
    draw_image_in_square(0, 5, ayaya)
    for row in range(1, rows):
        for column in range(columns):
            # передавали в функцию, рисующую в ряде или колонке текущий ряд, 
            # текущий столб,
            # тут только вызываем draw_image_in_square
            if mas[row][column] == 1:
                draw_image_in_square(row, column, ayaya)
            else:
                # вместо белого прямоугольника рисуем белую картинку
                draw_image_in_square(row, column, white_square)


    # обновляет картинку
    pygame.display.update()

