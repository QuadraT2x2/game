import pygame
import sys
import random

from graphics_utils import draw_image_in_square, draw_portrait, draw_arrows
from images import kitten, pooch, cock, viper, tigress, ayaya, unknown, background, white_square, up, down, left,\
    right, assasin, warrior, prophet
from screen_config import margin, width, height, columns, rows, screen, screen_x, screen_y, status_bar
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
color_list = [black, white, red, green, blue, aqua, purple, yellow]
color_random = random.randint(0, len(color_list) - 1)
my_color_choice = color_list[color_random]
active_unit = None


def click_on_screen():
    global active_unit
    x_mouse, y_mouse = pygame.mouse.get_pos()
    print(f'x = {x_mouse} y = {y_mouse}')
    if x_mouse <= screen_x:
        column = min((columns - 1), x_mouse // (margin + width))
        row = min((rows - 1), y_mouse // (margin + height))
        print(f'row = {row} column = {column}')
        if isinstance(mas[row][column], Character) is True:
            active_unit = mas[row][column]
            print('1488')
        else:
            active_unit = None
            print('322')
    drawing_gui()


def drawing_gui():
    font = pygame.font.Font(None, 40)  # це шрифт и размер
    if active_unit is None:
        my_text = "Unit is not selected"
        pygame.draw.rect(screen, my_color_choice, [screen_x + ((status_bar - 220) // 2), margin, 220, 220], 0)
    else:
        my_text = repr(active_unit)  # передать текст
        draw_portrait(active_unit.image)
    text = font.render(my_text, True, purple)
    screen.blit(text, [screen_x + margin, 220 + (margin * 2)])
    x = screen_x + ((360 - 40) // 2)
    y = screen_y - 250
    draw_arrows(x, y, white_square)
    draw_arrows(x, y - 65, up)
    draw_arrows(x, y + 65, down)
    draw_arrows(x - 65, y, left)
    draw_arrows(x + 65, y, right)


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
    drawing_gui()
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
                draw_image_in_square(row, column, mas_item.image)
    # обновляет картинку
    pygame.display.update()
