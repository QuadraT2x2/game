import pygame
import sys

from graphics_utils import draw_image_in_square
from images import kitten, pooch, cock, viper, tigress, ayaya, unknown, background, white_square
from screen_config import margin, width, height, columns, rows, screen, screenx
from characters import Character
from arena_tester import characters, create_5_monsters_no_prop

pygame.init()

pygame.display.set_icon(ayaya)
pygame.display.set_caption('Erunda')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
aqua = (0, 255, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)


def click_on_screen():
    x_mouse, y_mouse = pygame.mouse.get_pos()
    print(f'x = {x_mouse} y = {y_mouse}')
    if x_mouse <= screenx:
        column = min((columns - 1), x_mouse // (margin + width))
        row = min((rows - 1), y_mouse // (margin + height))
        print(f'row = {row} column = {column}')
        mas[row][column] = characters[0]


my_list = create_5_monsters_no_prop
mas = [[None] * columns for i in range(rows)]
mas[2][1] = my_list[0]
mas[4][5] = my_list[1]
mas[3][3] = my_list[2]
mas[4][2] = my_list[3]
mas[1][0] = my_list[4]

while True:
    # добавить строчку, которая будет рисовать картинку.
    screen.blit(background, (0, 0))
    # добавить на новую зону в экране текстовое поле с текстом "hello, text!"
    font = pygame.font.Font(None, 75)  # це шрифт
    text = font.render("Hello, text!", True, purple)
    screen.blit(text, [screenx + margin, margin])
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_on_screen()
    # Отрисовка экрана
    # рисует наши квадратики и картинки
    for row in range(rows):
        for column in range(columns):
            # передавали в функцию, рисующую в ряде или колонке текущий ряд, 
            # текущий столб,
            # тут только вызываем draw_image_in_square
            mas_item = mas[row][column]
            if mas_item is None:
                draw_image_in_square(row, column, white_square)
            if isinstance(mas_item, Character) is True:
                draw_image_in_square(row, column, characters[0].image)
    # обновляет картинку
    pygame.display.update()
