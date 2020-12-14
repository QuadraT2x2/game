import pygame
import sys
import random

from graphics_utils import draw_image_in_square, draw_portrait, draw_arrows
from images import kitten, pooch, cock, viper, tigress, ayaya, unknown, background, white_square, up, down, left,\
    right, assasin, warrior, prophet, stat_bar
from screen_config import margin, width, height, columns, rows, screen, screen_x, screen_y, status_bar
from characters import Character, Hero
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
active_row = None
active_column = None


def click_on_screen():
    global active_unit, active_row, active_column
    x_mouse, y_mouse = pygame.mouse.get_pos()
    print(f'x = {x_mouse} y = {y_mouse}')
    if x_mouse <= screen_x:
        column = min((columns - 1), x_mouse // (margin + width))
        row = min((rows - 1), y_mouse // (margin + height))
        print(f'row = {row} column = {column}')
        if isinstance(mas[row][column], Character) is True:
            active_unit = mas[row][column]
            active_row = row
            active_column = column
            print('1488')
        else:
            active_unit = None
            active_row = None
            active_column = None
            print('322')
    drawing_gui()


def motion_up():
    # active_row = 0
    # active_column = 0
    print('up')
    global active_unit, mas, active_column, active_row
    if active_column is not None:
        if (active_row - 1) < 0:
            print("движение не возможно")
        else:
            print(active_row, active_column)
            tmp = mas[active_row - 1][active_column]
            if isinstance(tmp, Character) is True:
                print("ячейка занята", tmp)
            else:
                mas[active_row - 1][active_column], mas[active_row][active_column] = mas[active_row][active_column],\
                                                                                     mas[active_row - 1][active_column]
                mas[active_row - 1][active_column] = active_unit
                active_row -= 1


def motion_down():
    print('down')
    global active_unit, mas, active_column, active_row
    if active_column is not None:
        if (active_row + 1) > (rows - 1):
            print("движение не возможно")
        else:
            if isinstance(mas[active_row + 1][active_column], Character) is True:
                print("ячейка занята")
            else:
                mas[active_row + 1][active_column], mas[active_row][active_column] = mas[active_row][active_column],\
                                                                                     mas[active_row + 1][active_column]
                mas[active_row + 1][active_column] = active_unit
                active_row += 1


def motion_left():
    print('left')
    global active_unit, mas, active_column, active_row
    if (active_column - 1) < 0:
        print("движение не возможно")
    else:
        if isinstance(mas[active_row][active_column - 1], Character) is True:
            print("ячейка занята")
        else:
            mas[active_row][active_column - 1], mas[active_row][active_column] = mas[active_row][active_column],\
                                                                                 mas[active_row][active_column - 1]
            mas[active_row][active_column - 1] = active_unit
            active_column -= 1


def motion_right():
    print('right')
    global active_unit, mas, active_column, active_row
    if (active_column + 1) > (columns - 1):
        print("движение не возможно")
    else:
        if isinstance(mas[active_row][active_column + 1], Character) is True:
            print("ячейка занята")
        else:
            mas[active_row][active_column + 1], mas[active_row][active_column] = mas[active_row][active_column],\
                                                                                 mas[active_row][active_column + 1]
            mas[active_row][active_column + 1] = active_unit
            active_column += 1


def motion(event):
    # print(f'paehali event.type = {event.type}')
    # я получаю события нажатия кнопки,
    if event.type == pygame.KEYDOWN:
        # уточняю что кнопка стрелка вверх
        if event.key == pygame.K_UP:
            # если я нажимаю стрелку вверх то вызывается движение вверх
            motion_up()
        elif event.key == pygame.K_DOWN:
            motion_down()
        elif event.key == pygame.K_LEFT:
            motion_left()
        elif event.key == pygame.K_RIGHT:
            motion_right()


def drawing_gui():
    font = pygame.font.Font(None, 40)  # це шрифт и размер
    if active_unit is None:
        my_text = "Unit is not selected"
        pygame.draw.rect(screen, my_color_choice, [screen_x + ((status_bar - 220) // 2), margin * 2, 220, 220], 0)
        text = font.render(my_text, True, purple)
    else:
        # хочу выводить статистику персонажа и героя. если герой дополнительный столбец с характеристиками
        if isinstance(active_unit, Hero):
            # изменить вывод текста
            # тут колонка статов "имя", "атака", "хп", "макс хп"
            # плюс статы "агила" "сила" "интелект"
            my_text = repr(active_unit)  # передать текст
            draw_portrait(active_unit.image)
            text = font.render(my_text, True, purple)
        elif isinstance(active_unit, Character):
            # изменить вывод текста
            # тут колонка статов "имя", "атака", "хп", "макс хп"
            my_text = repr(active_unit)  # передать текст
            draw_portrait(active_unit.image)
            text = font.render(my_text, True, purple)


    screen.blit(text, [screen_x + (margin * 2), 220 + (margin * 3)])
    x = screen_x + ((status_bar - 40) // 2)
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
    screen.blit(stat_bar, (screen_x, 0))
    # добавить на новую зону в экране текстовое поле с текстом "hello, text!"
    drawing_gui()
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_on_screen()
        motion(event)
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
