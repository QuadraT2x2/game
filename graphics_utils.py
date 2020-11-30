import pygame
from screen_config import margin, width, height, screen, screen_x, screen_y, screen_x_new, status_bar


def draw_image_in_square(square_row, square_column, image):
    square_x = margin + (margin + width) * square_column
    square_y = margin + (margin + height) * square_row
    screen.blit(image, (square_x, square_y))


def draw_portrait(image, x=screen_x + ((status_bar - 220) // 2), y=margin * 2):
    image = pygame.transform.scale(image, (220, 220))
    screen.blit(image, (x, y))


def draw_arrows(x, y, image):
    image = pygame.transform.scale(image, (40, 40))
    screen.blit(image, (x, y))
