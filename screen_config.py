import pygame

width = height = 110
columns = rows = 6
margin = 25

screen_x = (width * columns) + (margin * (columns + 1))
status_bar = 360
screen_x_new = screen_x + status_bar
screen_y = (height * rows) + margin * (rows + 1)

screen = pygame.display.set_mode((screen_x_new, screen_y))
